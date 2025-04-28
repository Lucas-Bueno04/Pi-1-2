import os
from dotenv import load_dotenv

load_dotenv()

db_host = str(os.getenv("DB_HOST"))
db_user = str(os.getenv("DB_USER"))
db_password = str(os.getenv("DB_PASSWORD"))
db_port = int(os.getenv("DB_PORT"))
db_name = str(os.getenv("DB_NAME"))

