from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView

from .views import RegisterAPI, MyObtainTokenPairView, Logout
from knox import views as knox_views


urlpatterns = [

    path('api/logout/', Logout.as_view(), name='logout'),
    path('api/loginall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/login/', MyObtainTokenPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path("api/register", RegisterAPI.as_view(), name="register")
]