import os

class Settings:
    # URI de conexión a MongoDB
    MONGO_URI: str = os.getenv("MONGO_URI", "mongodb://mongo:27017")

    # Nombre de la base de datos
    DATABASE_NAME: str = os.getenv("DATABASE_NAME", "users_db")

    # Clave secreta usada para tokens o sesiones
    SECRET_KEY: str = os.getenv("SECRET_KEY", "supersecreto")

    # Algoritmo usado para firmar tokens JWT
    ALGORITHM: str = os.getenv("ALGORITHM", "HS256")

# Instancia global de configuración
settings = Settings()
