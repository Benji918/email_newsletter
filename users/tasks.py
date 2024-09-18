from celery import shared_task
from core.models import MessageBoard
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from datetime import datetime

@shared_task(name='email_newsletter')
def send_newsletter():
    pass