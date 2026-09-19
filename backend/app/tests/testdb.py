from sqlalchemy import text

from app.database import engine

try:
    with engine.connect() as conn:
        result = conn.execute(text("SELECT 1"))
        print("Connected!")
        print(result.scalar())
except Exception as e:
    print("Connection failed")
    print(e)