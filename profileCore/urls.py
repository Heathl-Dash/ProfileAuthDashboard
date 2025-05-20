from django.urls import path
from . import views
from .api.api_views import ProfileApiView
urlpatterns=[
    # path('',views.home,name='home'),
    path('profile_api',ProfileApiView.as_view(),name='profile_api'),
    path('logout',views.logout,name='logout'),
]