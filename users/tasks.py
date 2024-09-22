from celery import shared_task
from core.models import MessageBoard
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime

@shared_task(name='email_newsletter')
def send_newsletter():
    subject = "Your Monthly Newsletter"
    
    subscribers = MessageBoard.objects.get(id=1).subscribers.filter(
        newsletter_subscribed=True,
    )
    
    for subscriber in subscribers:
        body = render_to_string('templates/newsletter.html', {'name': subscriber.username})
        email = EmailMessage( subject, body, to=[subscriber.email] )
        email.content_subtype = "html"
        email.send()
    
    current_month = datetime.now().strftime('%B') 
    subscriber_count = subscribers.count()   
    return f'{current_month} Newsletter to {subscriber_count} subs'