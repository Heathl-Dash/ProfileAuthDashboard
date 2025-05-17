from rest_framework.generics import  ListAPIView
from .serializers import DashboardProfileSerializer
from ..models import DashboardProfile

class ProfileApiView(ListAPIView):
    serializer_class=DashboardProfileSerializer
    queryset=DashboardProfile.objects.all()
    