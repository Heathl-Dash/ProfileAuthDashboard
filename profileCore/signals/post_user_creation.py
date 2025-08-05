from django.db.models.signals import post_save
from django.dispatch import receiver
from ..models import DashboardProfile
from profileAuth.amqp.publisher import create_user_publish_exchange


@receiver(post_save, sender=DashboardProfile)
def post_user_creation(sender, instance, created,**kwargs):
    user_id = instance.id
    if not user_id:
        create_user_publish_exchange(user_id)

