from rest_framework.generics import  ListAPIView
from .serializers import DashboardProfileSerializer,DashboardProfileTokenObtainPairSerializer,DashboardProfileTokenRefreshSerializer
from ..models import DashboardProfile

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

class ProfileApiView(ListAPIView):
    serializer_class=DashboardProfileSerializer
    queryset=DashboardProfile.objects.all()
    
class DashboardProfileTokenObtainPairView(TokenObtainPairView):
    serializer_class = DashboardProfileTokenObtainPairSerializer

class DashboardProfileTokenRefreshView(TokenRefreshView):
    serializer_class = DashboardProfileTokenRefreshSerializer