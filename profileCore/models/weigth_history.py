from django.db import models
from .dashboardprofile import DashboardProfile


class WeigthHistory(models.Model):
    weigth=models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=5)
    profile=models.ForeignKey(DashboardProfile,on_delete=models.CASCADE)
    imc_on_date=models.DecimalField(blank=True,null=True,decimal_places=2,max_digits=5)
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        formated_date = self.created_at.strftime('%d/%m/%y')
        return f"{self.profile.name}: {self.weigth}kg em {formated_date}"
    
    class Meta:
        ordering = ['-created_at']