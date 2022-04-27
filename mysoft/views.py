from django.contrib import messages
from django.contrib.auth import login, authenticate, logout
from django.shortcuts import redirect
from knox.models import AuthToken
from rest_framework import generics, status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth.models import User

from .serializers import MyTokenObtainPairSerializer, LogoutSerializer
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework_simplejwt.views import TokenObtainPairView


from .serializers import RegisterSerializer, UserSerializer


class RegisterAPI(generics.GenericAPIView):
	serializer_class = RegisterSerializer

	def post(self, request, *args, **kwargs):
		serializer = self.get_serializer(data=request.data)
		serializer.is_valid(raise_exception=True)
		user = serializer.save()
		return Response({
			"user": UserSerializer(user, context=self.get_serializer_context()).data,
			"token": AuthToken.objects.create(user)[1]
		})


class MyObtainTokenPairView(TokenObtainPairView):
	permission_classes = (AllowAny,)
	serializer_class = MyTokenObtainPairSerializer

	def post(self, request, *args, **kwargs):
		username = request.data.get("username")
		password = request.data.get("password")
		serializer = MyTokenObtainPairSerializer(data=self.request.data,
												 context={'request': self.request})
		serializer.is_valid(raise_exception=True)
		user = authenticate(username=username, password=password)
		if user is not None:
			login(request, user)
			messages.success(request, f' welcome {username} !!')
			return Response(self.get_tokens_for_user(user), status= status.HTTP_201_CREATED)
		else:
			return Response(status=status.HTTP_400_BAD_REQUEST)


	def get_tokens_for_user(self, user):
		refresh = RefreshToken.for_user(user)
		return {
			'refresh': str(refresh),
			'access': str(refresh.access_token),
		}


class ProfileView(generics.RetrieveAPIView):
	serializer_class = UserSerializer

	def get_object(self):
		return self.request.user


class Logout(APIView):
	permission_classes = [IsAuthenticated, ]
	serializer_class = LogoutSerializer
	queryset = User.objects.all()

	def post(self, request):
		serializer = self.serializer_class(data=request.data)
		serializer.is_valid(raise_exception=True)
		token = RefreshToken(request.data.get('refresh'))
		token.blacklist()
		logout(request)
		return Response("Success", status=status.HTTP_401_UNAUTHORIZED)
