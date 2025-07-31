from django.urls import path, include
from . import views
from .viewsets import (
    DashboardProfileTokenObtainPairView,
    DashboardProfileTokenRefreshView,
    CreateDashboardProfile,
    UpdateDashboardProfile,
    RetrieveProfile,
    DestroyProfile,
    CheckProfile,
    WeigthHistoryViewSet,
    WeigthMonthViewSet
)
from .views import GoogleAuthView

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r"weigth-history", WeigthHistoryViewSet, basename="weigth-history")
router.register(r"weigth-month", WeigthMonthViewSet, basename="weigth-month")
router.register(r"google-login", GoogleAuthView, basename="google-login")

urlpatterns = [
    path("createprofile/", CreateDashboardProfile.as_view(), name="createprofile"),
    path("retrieveprofile/", RetrieveProfile.as_view(), name="retireveprofile"),
    path("destroyprofile/", DestroyProfile.as_view(), name="destroyprofile"),
    path("updateprofile/", UpdateDashboardProfile.as_view(), name="updateprofile"),
    path("checkprofile/<int:user_id>/", CheckProfile.as_view(), name="checkprofile"),
    path(
        "token/",
        DashboardProfileTokenObtainPairView.as_view(),
        name="token_obtain_pair",
    ),
    path(
        "token/refresh/",
        DashboardProfileTokenRefreshView.as_view(),
        name="token_refresh",
    ),
    path("logout", views.logout, name="logout"),
    path("", include(router.urls)),
]
