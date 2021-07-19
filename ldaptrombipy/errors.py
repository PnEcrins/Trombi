from caldav.lib.error import NotFoundError

from flask import current_app
from werkzeug.exceptions import NotFound


@current_app.errorhandler(NotFoundError)
def caldav_notfound(error):
    print()
    raise NotFound("Not event found")
