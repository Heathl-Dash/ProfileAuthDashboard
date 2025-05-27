from rest_framework.generics import  ListAPIView
from rest_framework.views import APIView
from .serializers import DashboardProfileSerializer,DashboardProfileTokenObtainPairSerializer,DashboardProfileTokenRefreshSerializer
from ..models import DashboardProfile
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

class ProfileApiView(ListAPIView):
    serializer_class=DashboardProfileSerializer
    queryset=DashboardProfile.objects.all()
    
class DashboardProfileTokenObtainPairView(TokenObtainPairView):
    serializer_class = DashboardProfileTokenObtainPairSerializer

class DashboardProfileTokenRefreshView(TokenRefreshView):
    serializer_class = DashboardProfileTokenRefreshSerializer

class CheckProfile(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, user_id, format=None):
        try:
            user = DashboardProfile.objects.get(id=user_id)
            return Response({'exists': True}, status=status.HTTP_200_OK)
        except DashboardProfile.DoesNotExist:
            return Response({'exists': False}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
class RetrieveProfile(APIView):
    permission_classes=[IsAuthenticated]

    def get(self, request, format=None):
        try:
            user = request.user
            userserialized=DashboardProfileSerializer(user,many=False)
            return Response(userserialized.data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        