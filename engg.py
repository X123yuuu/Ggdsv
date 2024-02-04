import smtplib
import ssl

# Set up your email account
server = 'smtp.gmail.com'
email_address = 'GoogleEmercengySupport.@gmail.com'
password = 'your_email_password'

# Connect to the SMTP server
context = ssl.create_default_context()
with smtplib.SMTP_SSL(server, 465, context=context) as server:
    server.login(email_address, password)

# Create the message
message = f' We detected strange activity to your account .For safety reasons ,please login to your account from here: http://127.0.0.1:8000  '

# Send the message
server.sendmail(email_address, ['summerjr2@gmail.com'], message)
