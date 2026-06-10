import random
import smtplib

def generate_otp():
    return str(random.randint(100000, 999999))

def send_otp_email(receiver_email, otp):
    sender_email = "YOUR EMAIL ADDRESS @gmail.com"
    app_password = "YOUR APP PASSWORD"

    message = f"Subject: OTP Verification\n\nYour OTP is {otp}"

    server = smtplib.SMTP("smtp.gmail.com", 587)
    server.starttls()
    server.login(sender_email, app_password)
    server.sendmail(sender_email, receiver_email, message)
    server.quit()

def verify_otp(real_otp):
    user_otp = input("Enter the OTP: ")
    return user_otp == real_otp