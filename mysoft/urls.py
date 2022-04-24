from django.urls import path
from .views import RegisterAPI, LoginAPI
from knox import views as knox_views


urlpatterns = [
    path('api/login/', LoginAPI.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/loginall/', knox_views.LogoutAllView.as_view(), name='logoutall'),


    path("api/register", RegisterAPI.as_view(), name="register")
]