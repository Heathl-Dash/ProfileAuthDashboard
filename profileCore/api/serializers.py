from rest_framework import serializers
from ..models import DashboardProfile
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer,TokenRefreshSerializer
from rest_framework import exceptions
from ..models import DashboardProfile
from django.contrib.auth.password_validation import validate_password

class DashboardProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = DashboardProfile        
        fields = ['id', 'name', 'email', 'password','weigth','heigth','age',
                  'calc_IMC','imc_classification','imc_degree']
        
        extra_kwargs = {'password': {'write_only': True},'id':{'read_only': True}}    

class DashboardProfileCreateSerializer(serializers.ModelSerializer):
    password=serializers.CharField(write_only=True,required=True,validators=[validate_password])
    password2=serializers.CharField(write_only=True,required=True)
    class Meta:
        model=DashboardProfile
        fields = ['name', 'email', 'password','password2','weigth','heigth','age','emergency_phone_number','blood_type']
    def validate(self, attrs):
        if attrs['password']!=attrs['password2']:
            raise serializers.ValidationError('senhas não coincidem')
        return attrs
    
    def create(self, validated_data):
        validated_data.pop('password2')

        return DashboardProfile.objects.create_user(**validated_data)
    
class DashboardProfileTokenObtainPairSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        authenticate_kwargs={
            'email':attrs['email'],
            'password':attrs['password'],
        }

        try:
            authenticate_kwargs['request']=self.context['request']
        except KeyError:
            pass

        try:
            self.user = DashboardProfile.objects.get(email=authenticate_kwargs['email'])
            if not self.user.check_password(authenticate_kwargs['password']):
                raise exceptions.AuthenticationFailed('Credenciais inválidas')
        except DashboardProfile.DoesNotExist:
            raise exceptions.AuthenticationFailed('Usuário não encontrado')
        
        if not self.user.is_active:
            raise exceptions.AuthenticationFailed('Conta desativada')
        
        data = {}
        refresh = self.get_token(self.user)

        data['DashboardProfileRefresh'] = str(refresh)
        data['DashboardProfileAccess'] = str(refresh.access_token)

        return data

class DashboardProfileTokenRefreshSerializer(TokenRefreshSerializer):
    refresh=None
    DashboardProfileRefresh=serializers.CharField(required=True)
    def validate(self, attrs):
        attrs['refresh'] = attrs['DashboardProfileRefresh']
        
        data = super().validate(attrs)
        
        return {
            'DashboardProfileAccess': data['access'],
            'DashboardProfileRefresh': data.get('refresh', None) 
        }

        