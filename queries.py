from db import database


async def get_all_users():
    query = "SELECT * FROM users;"
    users = await database.fetch_all(query)
    result = []
    for user in users:
        query_workplaces = f"SELECT * FROM work_places WHERE user_id={user.get('id')}"
        workplaces = await database.fetch_all(query_workplaces)
        workplaces_by_user = []
        for workplace in workplaces:
            workplaces_by_user.append(
                {
                    "id": workplace.get('id'),
                    "address": workplace.get('address')
                }
            )

        result.append(
            {
                "id": user.get('id'),
                "username": user.get("username"),
                "workplaces": workplaces_by_user
            }
        )

    return result


async def get_one_user(user_id: int):
    query = f"SELECT * FROM users WHERE id={user_id};"
    user = await database.fetch_one(query)

    result = []

    if user is not None:
        query_workplaces = f"SELECT * FROM work_places WHERE user_id={user.get('id')}"
        workplaces = await database.fetch_all(query_workplaces)
        workplaces_by_user = []
        for workplace in workplaces:
            workplaces_by_user.append(
                {
                    "id": workplace.get('id'),
                    "address": workplace.get('address')
                }
            )

        result.append(
            {
                "id": user.get('id'),
                "username": user.get("username"),
                "workplaces": workplaces_by_user
            }
        )

    return result
