import segno
import sys
import sendEmail as sender
import time

#print (sys.argv[1])
data = sys.argv[1]
print('Created the QR Code!')

qrcode = segno.make_qr(data)
qrcode.save('./booking_record.png', scale=10)

sender.send()

time.sleep(5)