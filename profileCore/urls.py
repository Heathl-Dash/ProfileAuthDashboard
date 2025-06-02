from django.urls import path
from . import views
from .api.api_views import (DashboardProfileTokenObtainPairView,DashboardProfileTokenRefreshView,
                            CheckProfile,RetrieveProfile,CreateDashboardProfile,UpdateDashboardProfile,DestroyProfile)

urlpatterns=[
    path('createprofile/', CreateDashboardProfile.as_view(), name='createprofile'),
    path('retrieveprofile/', RetrieveProfile.as_view(), name='retireveprofile'),
    path('destroyprofile/', DestroyProfile.as_view(), name='destroyprofile'),
    path('updateprofile/', UpdateDashboardProfile.as_view(), name='updateprofile'),
    path('checkprofile/<int:user_id>/', CheckProfile.as_view(), name='checkprofile'),
    path('token/', DashboardProfileTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', DashboardProfileTokenRefreshView.as_view(), name='token_refresh'),
    path('logout',views.logout,name='logout'),
]