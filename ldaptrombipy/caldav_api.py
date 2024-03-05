from datetime import datetime, timedelta


from caldav import DAVClient
from flask import Blueprint, request
from ics import Calendar, Event
from flask.json import jsonify

from ldaptrombipy.config import CALDAV_PASSWORD, CALDAV_SERVER, CALDAV_USERNAME

blueprint = Blueprint("caldav", __name__)


@blueprint.route("/<email>")
def user_cal(email):
    filters = request.args
    client = DAVClient(
        url=CALDAV_SERVER,
        username=CALDAV_USERNAME,
        password=CALDAV_PASSWORD,
    )
    url = f"{CALDAV_SERVER}{email}/Calendar"
    calendar = client.calendar(url=url)

    if "start" in filters and "end" in filters:
        start = datetime.fromisoformat(filters["start"])
        end = datetime.fromisoformat(filters["end"])
    else:
        start = datetime.now()
        end = start + timedelta(days=7)
    # CalDav Events object have no start and end properties
    # we must pass throw ICS lib to build Calendar object for each event
    list_of_events = []
    for ics in calendar.date_search(start=start, end=end, expand="maybe"):
        # HACK : STATUS:NEEDS-ACTION make bug the Calendar obj
        str_event = ics.data.replace("STATUS:NEEDS-ACTION", "STATUS:TENTATIVE")
        cal = Calendar(str_event)
        event = list(cal.events)[0]
        if event.classification == "PRIVATE":
            continue
        begin = event.begin
        end = event.end
        # HACK because of bad support of reccurent event in zimbra https://caldav.readthedocs.io/en/latest/index.html?highlight=start#compatibility
        if event.all_day and "RECURRENCE-ID" in str_event:
            begin = event.end
            end = None
        event_as_dict = {
            "title": event.name,
            "id": event.uid,
            "description": event.description,
            "start": str(begin),
            "end": str(end),
            "begin_str": event.begin.datetime.strftime("%d/%m/%Y %H:%M"),
            "end_str": event.end.datetime.strftime("%d/%m/%Y %H:%M") if end else "",
            "allDay": event.all_day,
            "editable": False,
            "location": event.location,
            "organizer": f"{event.organizer.common_name if event.organizer else None}",
            "attendees": [
                f"{att.common_name} ({att.email})" for att in event.attendees
            ],
        }
        list_of_events.append(event_as_dict)
    return jsonify(list_of_events)
