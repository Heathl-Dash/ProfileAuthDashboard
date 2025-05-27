from django.urls import path
from . import views
from .api.api_views import ProfileApiView,DashboardProfileTokenObtainPairView,DashboardProfileTokenRefreshView
urlpatterns=[
    # path('',views.home,name='home'),
    path('profile_api',ProfileApiView.as_view(),name='profile_api'),
    path('token/', DashboardProfileTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', DashboardProfileTokenRefreshView.as_view(), name='token_refresh'),
    path('logout',views.logout,name='logout'),
]