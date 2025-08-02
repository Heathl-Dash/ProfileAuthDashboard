from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Profile API",
        default_version="1.0.0",
        description="Documentação API Perfil",
    ),
    public=True,
    permission_classes=[permissions.IsAdminUser],
)
urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    path(
        "api/v1/",
        include(
            [
                path("profiles/", include("profileCore.urls")),
                path(
                    "swagger/schema/",
                    schema_view.with_ui("swagger", cache_timeout=0),
                    name="swagger-schema",
                ),
            ]
        ),
    ),
]
