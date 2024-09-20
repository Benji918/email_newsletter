from django.db.models.signals import post_save
from django.dispatch import receiver
from core.models import CustomUser, MessageBoard

@receiver(post_save, sender=CustomUser)
def add_user_to_message_board(sender, instance, created, **kwargs):
    if created:
        # Automatically create a MessageBoard instance if none exists
        message_board, created = MessageBoard.objects.get_or_create(id=1)
        
        # Add the user to the message board subscribers if they subscribe to the newsletter
        if instance.newsletter_subscribed:
            message_board.subscribers.add(instance)
            message_board.save()
