from rest_framework.generics import  CreateAPIView,UpdateAPIView,DestroyAPIView,RetrieveAPIView
from rest_framework.views import APIView
from .serializers import DashboardProfileSerializer,DashboardProfileTokenObtainPairSerializer,DashboardProfileTokenRefreshSerializer,DashboardProfileCreateSerializer
from ..models import DashboardProfile
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status

from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView
from rest_framework_simplejwt.tokens import RefreshToken

class CreateDashboardProfile(CreateAPIView):
    serializer_class=DashboardProfileCreateSerializer
    permission_classes=[AllowAny]

    def create(self, request, *args, **kwargs):
        serializer=self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        profile=serializer.save()
        refresh=RefreshToken.for_user(profile)
        
        return Response({
            'DashboardProfileAccess':str(refresh.access_token),
            'DashboardProfileRefresh':str(refresh),
        },status=status.HTTP_201_CREATED)
    
class UpdateDashboardProfile(UpdateAPIView):
    serializer_class=DashboardProfileSerializer

    def get_object(self):
        return self.request.user

class DestroyProfile(DestroyAPIView):
    serializer_class=DashboardProfileSerializer
    def get_object(self):
        return self.request.user

class RetrieveProfile(RetrieveAPIView):
    serializer_class=DashboardProfileSerializer
    def get_object(self):
        return self.request.user
    
class DashboardProfileTokenObtainPairView(TokenObtainPairView):
    serializer_class = DashboardProfileTokenObtainPairSerializer

class DashboardProfileTokenRefreshView(TokenRefreshView):
    serializer_class = DashboardProfileTokenRefreshSerializer

class CheckProfile(APIView):
    def get(self, request, user_id, format=None):
        try:
            user = DashboardProfile.objects.get(id=user_id)
            if user!=request.user:
                return Response(status=status.HTTP_403_FORBIDDEN)
            return Response({'exists': True}, status=status.HTTP_200_OK)
        except DashboardProfile.DoesNotExist:
            return Response({'exists': False}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)
        

        