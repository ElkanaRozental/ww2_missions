from config.base import session_factory
from sqlalchemy import text


def create_tables():
    with session_factory() as session:
        session.execute(text("""create table if not exists priority (
                id serial primary key,
                priority varchar(100) unique)
            """))
        session.execute(text("""create table if not exists countries (
                id serial primary key,
                name varchar(200) unique not null)
            """))
        session.execute(text("""create table if not exists cities(
                id serial primary key,
                name varchar(200) unique not null)
            """))
        session.execute(text("""create table if not exists locations(
                id serial primary key,
                latitude decimal(12,8),
                longitude decimal(12,8)
                )
            """))
        session.execute(text("""create table if not exists target_type(
                id serial primary key,
                type varchar(200) unique not null
                )
            """))
        session.execute(text("""create table if not exists target_industry(
                id serial primary key,
                industry varchar(450) unique not null
                )
            """))
        session.execute(text("""create table if not exists normalized_mission(
                id serial primary key,
                country_id int,
                city_id int, 
                location_id int, 
                target_type_id int,
                target_industry_id int, 
                priority_id int, 
                foreign key (country_id) references countries(id) on delete cascade,
                foreign key (city_id) references cities(id) on delete cascade,
                foreign key (location_id) references locations(id) on delete cascade,
                foreign key (target_type_id) references target_type(id) on delete cascade,
                foreign key (target_industry_id) references target_industry(id) on delete cascade,
                foreign key (priority_id) references priority(id) on delete cascade
                )
            """))
        session.commit()


def insert_data_from_unnormalized():
    with session_factory() as session:
        session.execute(text("""insert into countries (name)
            select distinct target_country
            FROM mission
            where target_country is not NULL
            on conflict (name) do nothing;
            """))
        session.execute(text("""insert into cities (name)
            select distinct target_city
            FROM mission
            where target_city is not NULL
            on conflict (name) do nothing;
            """))
        session.execute(text("""INSERT INTO locations (latitude, longitude)
            SELECT DISTINCT target_latitude, target_longitude
            FROM mission m
            WHERE target_latitude IS NOT NULL 
              AND target_longitude IS NOT NULL
              AND NOT EXISTS (
                  SELECT 1 
                  FROM locations l
                  WHERE l.latitude = m.target_latitude
                    AND l.longitude = m.target_longitude
              );
            """))
        session.execute(text("""INSERT INTO target_type (type)
            SELECT DISTINCT target_type
            FROM mission 
            WHERE target_type IS NOT NULL 
            on conflict (type) do nothing;
              
            """))
        session.execute(text("""INSERT INTO target_industry (industry)
            SELECT DISTINCT target_industry
            FROM mission 
            WHERE target_industry IS NOT NULL 
            on conflict (industry) do nothing;
              
            """))
        session.execute(text("""insert into priority (priority)
            select distinct target_priority
            FROM mission
            where target_priority is not NULL
            on conflict (priority) do nothing;
                    """))
        session.execute(text("""
            insert into normalized_mission (
                country_id, city_id, location_id, target_type_id, target_industry_id, priority_id
            )
            select distinct 
                co.id, 
                ci.id, 
                lo.id,          
                tt.id,
                ti.id,
                p.id
            from mission m
            join cities ci on m.target_city = ci.name
            join countries co on m.target_country = co.name
            join locations lo on m.target_longitude = lo.longitude and m.target_latitude = lo.latitude
            join target_type tt on tt.type = m.target_type
            join target_industry ti on ti.industry = m.target_industry
            join priority p on m.target_priority = p.priority
           """))
