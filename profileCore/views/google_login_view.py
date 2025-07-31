import os
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from google.oauth2 import id_token
from google.auth.transport import requests as google_requests
from django.utils.crypto import get_random_string
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

User = get_user_model()

class GoogleAuthView(APIView):
    def post(self, request):
        token = request.data.get("token")
        if not token:
            return Response({"error": "Token não enviado"}, status=status.HTTP_400_BAD_REQUEST)

        try:
            idinfo = id_token.verify_oauth2_token(
                token,
                google_requests.Request(),
                os.environ.get("DB_ENGINE")
            )

            email = idinfo["email"]
            name = idinfo.get("name", "")

            user, created = User.objects.get_or_create(
                email=email,
                defaults={
                    "name": name,
                    "password": get_random_string(64),
                }
            )

            refresh = RefreshToken.for_user(user)
            return Response({
                "DashboardProfileRefresh": str(refresh),
                "DashboardProfileAccess": str(refresh.access_token),
            })
        except ValueError:
            return Response({"error": "Token do Google inválido"}, status=status.HTTP_400_BAD_REQUEST)
