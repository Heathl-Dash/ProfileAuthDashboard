from django.db import models
from .dashboardprofile import DashboardProfile


class MonthWeigth(models.Model):
    weigth = models.DecimalField(blank=True, null=True, decimal_places=2, max_digits=5)
    profile = models.ForeignKey(DashboardProfile, on_delete=models.CASCADE)
    imc_on_date = models.DecimalField(
        blank=True, null=True, decimal_places=2, max_digits=5
    )
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed=False
        db_table="mv_weigth_history_monthly_mv"
        ordering = ["-created_at"]