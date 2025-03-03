from .models import ChatMessage
from django.db.models.signals import post_save
from django.dispatch import receiver

@receiver(post_save, sender=ChatMessage)
def set_chat_session_title(sender, instance, **kwargs):
    session = instance.session
    if not session.title:  # Only set title if it doesn't already exist
        session.title = instance.message[:50]
        session.save()
