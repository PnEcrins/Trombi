from flask.json.provider import DefaultJSONProvider
from flask import Flask
from ldap3.utils.ciDict import CaseInsensitiveDict
from flask_cors import CORS

from ldaptrombipy import config


class CustomJsonEncoder(DefaultJSONProvider):
    def default(self, obj):
        if isinstance(obj, CaseInsensitiveDict):
            return dict(obj)


def create_app():
    app = Flask(__name__)
    with app.app_context():
        app.json = CustomJsonEncoder(app)
        from ldaptrombipy.ldpap_api import blueprint
        from ldaptrombipy import errors

        app.register_blueprint(blueprint)

        from ldaptrombipy.caldav_api import blueprint

        app.register_blueprint(blueprint, url_prefix="/caldav")
        CORS(app, supports_credentials=True)
    return app


if __name__ == "__main__":
    app = create_app()
    app.run(port=config.API_PORT)
