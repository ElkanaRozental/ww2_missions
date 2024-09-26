from typing import Dict

from returns.maybe import Maybe, Nothing, Some
import toolz as t
from sqlalchemy import inspect
from model import NormalizedMission
from service.utils import has_all_keys


def create_mission(mission_dict: Dict[str, str]) -> NormalizedMission:
    return NormalizedMission(
        country_id=mission_dict["country_id"],
        city_id=mission_dict["city_id"],
        location_id=mission_dict["location_id"],
        target_type_id=mission_dict["target_type_id"],
        target_industry_id = mission_dict["target_industry_id"],
        priority_id=mission_dict["priority_id"]
    )


def convert_to_mission(mission_json: Dict[str, str]) -> Maybe[NormalizedMission]:
    return t.pipe(
        mission_json,
        has_all_keys(['country_id', 'city_id', 'location_id', 'target_type_id', 'target_industry_id', 'priority_id']),
        lambda is_valid: Nothing if not is_valid else Some(create_mission(mission_json))
    )


def convert_to_json(mission: NormalizedMission) -> Dict[str, str]:
    return {c.key: getattr(mission, c.key) for c in inspect(mission).mapper.column_attrs}