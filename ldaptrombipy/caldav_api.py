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
        end_date = e.end.datetime
        if end_date.hour == 0 and end_date.minute == 0:
            end_date = end_date - timedelta(1)
            # 23h59 not work with fullcalendar ...
            end_date = end_date.replace(hour=20, minute=59)
        event_as_dict = {
            "title": e.name,
            "id": e.uid,
            "description": e.description,
            "start": str(e.begin),
            "end": str(end_date),
        }
        r.append(event_as_dict)
    return jsonify(r)
