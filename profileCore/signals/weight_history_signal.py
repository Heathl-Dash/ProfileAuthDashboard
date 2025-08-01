from django.db.models.signals import pre_save
from django.dispatch import receiver

from ..models import WeigthHistory, DashboardProfile


@receiver(pre_save, sender=DashboardProfile)
def create_weigth_history_after_profile_update(sender, instance, **kwargs):
    """Realiza ações após a model NomeDaSuaModel ser salva."""
    if not instance.pk:
        return
    else:
        try:
            oldprofile = sender.objects.get(pk=instance.pk)
        except:
            oldprofile = None

        if oldprofile and oldprofile.weigth != instance.weigth:
            create_weigth_history(profile=instance)


def create_weigth_history(profile: DashboardProfile):
    WeigthHistory.objects.create(
        weigth=profile.weigth, profile=profile, imc_on_date=profile.calc_IMC
    )
