#This file is used fro establishing configurations 
from dotenv import load_dotenv
import os
load_dotenv()
class Config():
    db_host = os.getenv("DB_HOST")
    db_port = os.getenv("DB_PORT")
    db_user = os.getenv("DB_USER")
    db_password = os.getenv("DB_PASSWORD")
    db_name = os.getenv("DB_NAME")
    from_email = os.getenv("EMAIL_ADDRESS") 
    email_app_password = os.getenv("EMAIL_APP_PASSWORD")
    print(db_host,db_name,db_password,db_port,db_user)
    


