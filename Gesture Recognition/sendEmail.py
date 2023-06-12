from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

def send():
    content = MIMEMultipart()  # 建立MIMEMultipart物件
    content["subject"] = "City Hotel Booking"  # 郵件標題
    content["from"] = "fyptesting2023@gmail.com"  # 寄件者
    content["to"] = "fungkingsh2@gmail.com"  # 收件者
    content.attach(MIMEText("Demo python send email"))  # 郵件純文字內容
    content.attach(MIMEImage(Path(r"C:\xampp\htdocs\project_new\booking_record.png").read_bytes()))  # 郵件圖片內容

    with smtplib.SMTP(host="smtp.gmail.com", port="587") as smtp:  # 設定SMTP伺服器
        try:
            smtp.ehlo()  # 驗證SMTP伺服器
            smtp.starttls()  # 建立加密傳輸
            smtp.login("fyptesting2023@gmail.com", "cqqcynngimhetfho")  # 登入寄件者gmail
            smtp.send_message(content)  # 寄送郵件
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)
