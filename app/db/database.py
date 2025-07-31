from motor.motor_asyncio import AsyncIOMotorClient
from app.core.config import settings

# Crear cliente de MongoDB de forma asíncrona
client = AsyncIOMotorClient(settings.MONGO_URI)

# Acceder a la base de datos especificada en configuración
db = client[settings.DATABASE_NAME]

# Colección específica para usuarios
users_collection = db["users"]
