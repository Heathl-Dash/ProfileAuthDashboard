from django.urls import path, include
from . import views
from .api.api_views import ProfileApiView

urlpatterns=[
    # path('',views.home,name='home'),
    path('profile_api',ProfileApiView.as_view(),name='profile_api'),
    path('logout',views.logout,name='logout'),
    path('accounts/', include('allauth.urls')),
    path('dj-rest-auth/', include('dj_rest_auth.urls')),
    path('dj-rest-auth/registration/', include('dj_rest_auth.registration.urls')),
]