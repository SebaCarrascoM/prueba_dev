from datetime import datetime
from uuid import uuid4
import jwt



SECRET_KEY = "supersecreto"


def build_user_dict(user):
    now = datetime.utcnow().isoformat()
    return {
        "id": str(uuid4()),
        "name": user["name"],
        "email": user["email"],
        "password": user["password"],
        "phones": user["phones"],
        "created": now,
        "modified": now,
        "last_login": now,
        "token": jwt.encode({"email": user["email"]}, SECRET_KEY, algorithm="HS256"),
        "isactive": True,
    }