from django.db.models.signals import post_delete
from django.dispatch import receiver
from .models import DashboardProfile
from profileAuth.amqp.publisher import delete_user_publish_event

@receiver(post_delete, sender=DashboardProfile)
def post_user_delete(sender, instance, **kwargs):
    user_id=instance.id
    if user_id:
        delete_user_publish_event(user_id)
