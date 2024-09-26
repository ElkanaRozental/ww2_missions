explain analyze select air_force, count(*) as mission_count
from mission m
where extract(year from mission_date) = 1943
group by air_force
order by mission_count desc
limit 1


create index air_force_index on mission using hash (air_force);
create index mission_date_index on mission using hash(mission_date)


--------------------------------------------------------------------


explain analyze select bomb_damage_assessment, count(target_country) from mission
where bomb_damage_assessment is not null
and airborne_aircraft > 5
group by target_country, bomb_damage_assessment
order by count(bomb_damage_assessment) desc limit 1


create index bomb_damage_assessment_index on mission(bomb_damage_assessment)
create index airborne_aircraft on mission(airborne_aircraft)