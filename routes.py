from fastapi import APIRouter, Depends
from fastapi import status, HTTPException

from auth import AuthHandler
from schemas import AuthDetails
from queries import get_all_users, get_one_user, create_user, get_users_with_passwords

router = APIRouter(tags=["Users"])

auth_handler = AuthHandler()


@router.post('/register', status_code=201)
async def register(auth_details: AuthDetails):
    users = await get_all_users()
    if any(user['username'] == auth_details.username for user in users):
        raise HTTPException(status_code=400, detail='Username is taken')
    hashed_password = auth_handler.get_password_hash(auth_details.password)

    await create_user(username=auth_details.username, password=hashed_password)
    return {"message": "Successfully Created!"}


@router.post('/login')
async def login(auth_details: AuthDetails):
    user = None
    users = await get_users_with_passwords()
    for x in users:
        if x['username'] == auth_details.username:
            user = x
            break

    if (user is None) or (not auth_handler.verify_password(auth_details.password, user['password'])):
        raise HTTPException(status_code=401, detail='Invalid username and/or password')
    token = auth_handler.encode_token(user['username'])
    return {'token': token}


@router.get("/users/")
async def get_users(username=Depends(auth_handler.auth_wrapper)):
    users = await get_all_users()
    return users


@router.get("/users/{id}/")
async def get_user(id: int, username=Depends(auth_handler.auth_wrapper)):
    user = await get_one_user(user_id=id)

    if not user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="user not found")

    return user
