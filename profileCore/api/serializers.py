from rest_framework import serializers
from ..models import DashboardProfile

class DashboardProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = DashboardProfile        
        fields = ['id', 'name', 'email', 'password','weigth','heigth','age',
                  'calc_IMC','imc_classification','imc_degree']
        
        extra_kwargs = {'password': {'write_only': True}}    
        