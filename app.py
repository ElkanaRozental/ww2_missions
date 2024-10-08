
from flask import Flask

from controller.normalized_mission_controller import mission_blueprint
from model import NormalizedMission
from repository.database import create_tables, insert_data_from_unnormalized


app = Flask(__name__)

if __name__ == '__main__':
    create_tables()
    insert_data_from_unnormalized()

    app.register_blueprint(mission_blueprint, url_prefix="/api/mission")
    app.run(debug=True, use_reloader=False)
