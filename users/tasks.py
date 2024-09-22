from celery import shared_task
from core.models import MessageBoard
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib, ssl
from django.conf import settings
from datetime import datetime
from email import encoders
from email.mime.base import MIMEBase
from django.template.loader import get_template
from django.core.mail import EmailMessage

@shared_task(name='email_newsletter')
def send_newsletter():
    subject = "Your Monthly Newsletter"
    
    subscribers = MessageBoard.objects.get(id=1).subscribers.filter(
        newsletter_subscribed=True,
    )
    
    for subscriber in subscribers:
        print(subscriber.email)
        message = get_template('newsletter.html').render(context={'name': subscriber.username})
        mail = EmailMessage(
            subject=subject, 
            body=message, 
            from_email=settings.EMAIL_HOST_USER,
            to=[subscriber.email],
            reply_to=[settings.EMAIL_HOST_USER],
            )
        mail.content_subtype = "html"
        mail.send()
    
    # print('task running!!!!!')
    # # Create a MIME object
    # msg = MIMEMultipart()
    # file_path = 'home/benji/email_newsletter/templates/newsletter.html'
    # for subscriber in subscribers:
    #     print(subscriber.email)
    #     # Attach the message
    #     msg.attach(MIMEText('Cheers to from me', "plain"))

    #     # Set the email subject, sender, and receiver
    #     msg["Subject"] = 'welcome to GFG world'
    #     msg["From"] = settings.EMAIL_HOST_USER
    #     msg["To"] = subscriber.email
        

    #      # Attach the file
    #     with open(file_path, "rb") as attachment:
    #         part = MIMEBase("application", "octet-stream")
    #         part.set_payload(attachment.read())

    #     # Encode the file in base64
    #     encoders.encode_base64(part)

    #     # Add header for the attachment
    #     part.add_header(
    #         "Content-Disposition",
    #         f"attachment; filename= {file_path.split('/')[-1]}",
    #     )

    #     # Attach the file to the message
    #     msg.attach(part)

    #     # Establish a connection to the SMTP server
    #     context = ssl.create_default_context()
    #     with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
    #         # Log in to the email account
    #         server.login(settings.EMAIL_HOST_USER, settings.EMAIL_HOST_PASSWORD)

    #         # Send the email
    #         server.sendmail(settings.EMAIL_HOST_USER, subscriber.email, msg.as_string())
    current_month = datetime.now().strftime('%B') 
    subscriber_count = subscribers.count()   
    return f'{current_month} Newsletter to {subscriber_count} subs'
