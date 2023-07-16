import segno
import sys
import sendEmail as sender
import time

data = sys.argv[1]
email = sys.argv[2]

qrcode = segno.make_qr(data)
qrcode.save('./booking_record.png', scale=10)

sender.send(email)

time.sleep(5)