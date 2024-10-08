from flask import Blueprint, request, jsonify
from repository.normalized_mission_repository import (
    insert_mission, find_mission_by_id, find_all_missions, delete_mission, update_mission
)

from service.normalized_mission_service import convert_to_mission, convert_to_json

mission_blueprint = Blueprint("mission", __name__)


@mission_blueprint.route("/create", methods=['POST'])
def create_mission():
    return (
        convert_to_mission(request.json)
        .bind(insert_mission)
        .map(convert_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 400))
    )


@mission_blueprint.route("/<int:m_id>", methods=['GET'])
def get_mission(m_id: int):
    return (
        find_mission_by_id(m_id)
        .map(convert_to_json)
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 404))
    )


@mission_blueprint.route("/", methods=['GET'])
def get_all():
    return (
        find_all_missions()
        .map(lambda missions: [convert_to_json(mission) for mission in missions])
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 404))
    )


@mission_blueprint.route("/delete/<int:u_id>", methods=['DELETE'])
def delete(m_id):
    return (
        delete_mission(m_id)
        .map(convert_to_json)
        .map(lambda u: (jsonify(u), 204))
        .value_or((jsonify({}), 404))
    )


@mission_blueprint.route("/update/<int:u_id>", methods=['PUT'])
def update(m_id):
    mission = convert_to_mission(request.json)
    return (
        update_mission(m_id, mission.unwrap())
        .map(convert_to_json)
        .map(lambda u: (jsonify(u), 204))
        .value_or((jsonify({}), 404))
    )

