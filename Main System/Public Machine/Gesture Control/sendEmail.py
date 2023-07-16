from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
import smtplib

def send(address):
    content = MIMEMultipart() 
    content["subject"] = "City Hotel Booking"  
    content["from"] = "fyptesting2023@gmail.com"  
    content["to"] = address
    content.attach(MIMEText("Thank you for your reservation! \n\n"
                            "A QR code is attached to this email. Please use this QR code to check in when using a public machine."))  
    content.attach(MIMEImage(Path(r"./booking_record.png").read_bytes()))  

    dome = address.split('@')[1]
    with smtplib.SMTP(host="smtp."+dome, port="587") as smtp:  
        try:
            smtp.ehlo() 
            smtp.starttls()  
            smtp.login("fyptesting2023@gmail.com", "cqqcynngimhetfho")  
            smtp.send_message(content) 
            print("Complete!")
        except Exception as e:
            print("Error message: ", e)

