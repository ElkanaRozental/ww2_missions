import logging

from flask import Flask

from controller.normalized_mission_controller import mission_blueprint
from model import NormalizedMission
from repository.database import create_tables


def create_app():
    flask_app = Flask(__name__)
    return flask_app


if __name__ == '__main__':
    create_tables()
    app = create_app()
    app.register_blueprint(mission_blueprint, url_prefix="/api/missions")
    app.run(debug=True, use_reloader=False)
