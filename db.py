import os

from databases import Database

from dotenv import load_dotenv

load_dotenv(dotenv_path='.env')

DB_USER = os.environ.get('DB_USER')
DB_PASSWORD = os.environ.get('DB_PASSWORD')
DB_HOST = os.environ.get('DB_HOST')
DB_NAME = os.environ.get('DB_NAME')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}/{DB_NAME}"

database = Database(DATABASE_URL)

# database.execute("""create table if not exists users
#     (
#         id bigserial constraint users_pk primary key,
#         username varchar(127),
#         password varchar(255) not null
# );
#
#
# """)
#
# database.execute("""
# create table if not exists work_places
#     (
#     id bigserial constraint work_places_pk primary key,
#     address varchar(127),
#     user_id bigint constraint work_places_users_id_fk references users on delete cascade
# );
#
# create unique index work_places_id_uindex
#     on work_places (id);
#
# """)
