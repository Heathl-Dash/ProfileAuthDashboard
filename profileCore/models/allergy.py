from django.db import models
from .dashboardprofile import DashboardProfile


class Allergy(models.Model):
    name = models.CharField(max_length=144)
    allergy_type = models.IntegerField(default=1)
    profile = models.ForeignKey(DashboardProfile, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
