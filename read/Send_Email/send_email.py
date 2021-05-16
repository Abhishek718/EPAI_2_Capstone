import email, smtplib, ssl
import time
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime


def send_emails(name,score,email,given_time = 30,course_name = 0,total = 0,):
    '''
    This is send_email.py file

    this is basically use to send an email to the respective person with their details and with attachment as a certificate

    this can have 6 arguments:
      1) name of a person
      2) score of a person
      3) email of a person 
      4) given_time which is basically wait time between the mail
      5) course_name
      6) total score of a course
	'''

    if course_name != 0:
        course_name = course_name
        total = total
    else:
        course_name = "Extensive Python & PyTorch for AI"
        total = "100"
    subject = "Congratulations...!!!"
    body = """\
Dear {name},

Congratulations! You have cleared the {course_name} with {score} marks out of {Total} marks!

We are excited to share the attached Award of Excellence for your performance!

Regards""".format(name=name,course_name=course_name,score=score,Total=total)
    sender_email = "abhishekqwerty919@gmail.com"
    receiver_email = email
    password = "Qwertyuiop1234567890"

    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject
    message["Bcc"] = receiver_email  # Recommended for mass emails
    date = datetime.datetime.now()
    # Add body to email
    message.attach(MIMEText(body, "plain"))

    filename = "generated_certificate\\{name}.jpg".format(name=name)  # In same directory as script
    attachment_name = "{name} {date}.jpg".format(name=name,date = date)

    # Open PDF file in binary mode
    with open(filename, "rb") as attachment:
        # Add file as application/octet-stream
        # Email client can usually download this automatically as attachment
        part = MIMEBase("application", "octet-stream")
        part.set_payload(attachment.read())

    # Encode file in ASCII characters to send by email    
    encoders.encode_base64(part)

    # Add header as key/value pair to attachment part
    part.add_header(
        "Content-Disposition",
        f"attachment; filename= {attachment_name}",
    )

    # Add attachment to message and convert message to string
    message.attach(part)
    text = message.as_string()

    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
    time.sleep(given_time)



