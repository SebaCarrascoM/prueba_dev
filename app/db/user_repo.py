from app.db.database import users_collection

async def find_user_by_email(email: str):
    """
    Busca un usuario en la base de datos por su dirección de correo electrónico.
    """
    return await users_collection.find_one({"email": email})

async def save_user(user_data: dict):
    """
    Guarda un nuevo usuario en la colección de usuarios.
    """
    await users_collection.insert_one(user_data)

async def get_all_users():
    users_cursor = users_collection.find()
    users = []
    async for user in users_cursor:
        user["id"] = str(user.get("id", user["_id"]))
        users.append(user)
    return users
