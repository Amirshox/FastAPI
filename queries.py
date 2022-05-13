from db import database


async def get_all_users():
    query = "SELECT * FROM users LEFT JOIN work_places ON users.id = work_places.user_id;"
    users = await database.fetch_all(query)

    return [{**user} for user in users]


async def get_one_user(user_id: int):
    query = f"SELECT * FROM users LEFT JOIN work_places ON users.id = work_places.user_id WHERE users.id=1;"
    user = await database.fetch_one(query)

    return user
