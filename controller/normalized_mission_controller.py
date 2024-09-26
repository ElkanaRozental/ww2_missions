from flask import Blueprint, request, jsonify
from repository.normalized_mission_repository import (
    insert_mission, find_mission_by_id, find_all_missions, delete_mission, update_missin
)
from service.user_service import convert_to_user, convert_to_json

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
        .map(lambda users: [convert_to_json(user) for user in users])
        .map(lambda u: (jsonify(u), 200))
        .value_or((jsonify({}), 404))
    )


@mission_blueprint.route("/delete/<int:u_id>", methods=['DELETE'])
def delete(u_id):
    return (
        delete_mission(u_id)
        .map(convert_to_json)
        .map(lambda u: (jsonify(u), 204))
        .value_or((jsonify({}), 404))
    )


@mission_blueprint.route("/update/<int:u_id>", methods=['PUT'])
def update(u_id):
    user = convert_to_user(request.json)
    return (
        update_missin(u_id, user.unwrap())
        .map(convert_to_json)
        .map(lambda u: (jsonify(u), 204))
        .value_or((jsonify({}), 404))
    )

