from datetime import datetime, timedelta

from ics import Calendar

# from ics import Calendar

from flask import Blueprint, request
from caldav import DAVClient
from ldaptrombipy.config import CALDAV_PASSWORD, CALDAV_SERVER, CALDAV_USERNAME
from flask.json import jsonify

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
    user_cal_str = ""
    if "start" in filters and "end" in filters:
        start = datetime.fromisoformat(filters["start"])
        end = datetime.fromisoformat(filters["end"])
    else:
        start = datetime.now()
        end = start + timedelta(days=7)
    list_of_calendar = []
    calender_with_all_events = Calendar()
    # CalDav Events object have no start and end properties
    # we must pass throw ICS lib to build Calendar object for each event
    for e in calendar.date_search(start=start, end=end, expand=True):
        user_cal_str = user_cal_str + e.data
        list_of_calendar.append(Calendar(e.data))
    for c in list_of_calendar:
        for event in c.events:
            calender_with_all_events.events.add(event)
    r = []
    for e in calender_with_all_events.events:
        event_as_dict = {
            "title": e.name,
            "id": e.uid,
            "description": e.description,
            "start": str(e.begin),
            "end": str(e.end),
            "begin_str": e.begin.datetime.strftime("%d/%m/%Y %H:%M"),
            "end_str": e.end.datetime.strftime("%d/%m/%Y %H:%M"),
            "allDay": e.all_day,
            "editable": False,
            "location": e.location,
            "organizer": f"{e.organizer.common_name} ({e.organizer.email})",
            "attendees": [f"{att.common_name} ({att.email})" for att in e.attendees]
        }
        r.append(event_as_dict)
    return jsonify(r)
