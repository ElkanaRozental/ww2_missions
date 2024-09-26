from typing import List

from returns.maybe import Maybe, Nothing
from returns.result import Result, Success, Failure
from sqlalchemy.exc import SQLAlchemyError

from config.base import session_factory
from model import NormalizedMission


def insert_mission(mission: NormalizedMission) -> Result[NormalizedMission, str]:
    with session_factory() as session:
        try:
            session.add(mission)
            session.commit()
            session.refresh(mission)
            return Success(mission)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def find_all_missions() -> Maybe[List[NormalizedMission]]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.query(NormalizedMission).all()
        )


def find_mission_by_id(m_id: int) -> Maybe[NormalizedMission]:
    with session_factory() as session:
        return Maybe.from_optional(
            session.get(NormalizedMission, m_id)
        )


def delete_mission(m_id: int) -> Result[NormalizedMission, str]:
    with session_factory() as session:
        try:
            maybe_mission = find_mission_by_id(m_id)
            if maybe_mission is Nothing:
                return Failure(f"No mission by the id: {m_id}")
            mission_to_delete = maybe_mission.unwrap()
            session.delete(mission_to_delete)
            session.commit()
            return Success(mission_to_delete)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))


def update_mission(m_id: int, details: NormalizedMission) -> Result[NormalizedMission, str]:
    with session_factory() as session:
        try:
            maybe_mission = find_mission_by_id(m_id)
            if maybe_mission is Nothing:
                return Failure(f"No mission by the id: {m_id}")
            mission_to_update = session.merge(maybe_mission.unwrap())
            mission_to_update.city_id = details.city_id
            mission_to_update.country_id = details.country_id
            mission_to_update.location_id = details.location_id
            mission_to_update.priority_id = details.priority_id
            mission_to_update.target_industry_id = details.target_industry_id
            mission_to_update.target_type_id = details.target_type_id
            session.commit()
            session.refresh(mission_to_update)
            return Success(mission_to_update)
        except SQLAlchemyError as e:
            session.rollback()
            return Failure(str(e))



