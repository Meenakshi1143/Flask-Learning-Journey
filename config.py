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
    # print(db_host,db_name,db_password,db_port,db_user)
    
class emailTemplates():

    def send_otp_template(otp: int, username: str):
        template = f"""
        <html>
        <body>
            <h2>Welcome to SNS!</h2>

            <p>Hi {username},</p>

            <p>To complete your registration, please use the OTP below:</p>

            <h2 style="color: blue;">{otp}</h2>

            <p>This OTP is valid for <b>3 minutes</b>.</p>

            <p>Please don't share this code with anyone.</p>

            <br>

            <p>Best Regards,<br>
            <b>SNS Team</b></p>
        </body>
        </html>
        """
        return template

    def send_reset_password_template(username: str, url: str, time: int):

        template = f"""
        <html>
        <body>
            <h2>Password Reset - SNS</h2>

            <p>Hi {username},</p>

            <p>We received a request to reset your SNS account password.</p>

            <p>Click the button below to reset your password:</p>

            <a href="{url}"
               style="background-color: blue;
                      color: white;
                      padding: 10px 20px;
                      text-decoration: none;">
                Reset Password
            </a>

            <p>This password reset link is valid for
            <b>{time} minutes</b>.</p>

            <p>If you did not request this password reset,
            you can safely ignore this email.</p>

            <br>

            <p>Best Regards,<br>
            <b>SNS Team</b></p>
        </body>
        </html>
        """

        return template
