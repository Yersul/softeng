from django.contrib.auth import authenticate, login
from django.contrib.auth.password_validation import validate_password
from django.http import Http404
from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    username = serializers.CharField(
        label="Username",
        write_only=True
    )
    password = serializers.CharField(
        label="Password",
        # This will be used when the DRF browsable API is enabled
        style={'input_type': 'password'},
        trim_whitespace=False,
        write_only=True
    )

    # @classmethod
    # def get_token(cls, user):
    #     token = super(MyTokenObtainPairSerializer, cls).get_token(user)
    #
    #     # Add custom claims
    #     token['username'] = user.username
    #     return token

    # def validate(self, attrs):
    #     # Take username and password from request
    #     username = attrs.get('username')
    #     password = attrs.get('password')
    #
    #     if username and password:
    #         # Try to authenticate the user using Django auth framework.
    #         user = authenticate(request=self.context.get('request'),
    #                             username=username, password=password)
    #         if not user:
    #             # If we don't have a regular user, raise a ValidationError
    #             msg = 'Access denied: wrong username or password.'
    #             raise serializers.ValidationError(msg, code='authorization')
    #     else:
    #         msg = 'Both "username" and "password" are required.'
    #         raise serializers.ValidationError(msg, code='authorization')
    #     # We have a valid user, put it in the serializer's validated_data.
    #     # It will be used in the view.
    #     attrs['user'] = user
    #     return attrs

    def login_user(self, request, user):
        login(request, user)
        return True


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
        )


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(write_only=True, required=True, validators=[validate_password])
    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = (
            'id',
            'username',
            'email',
            'first_name',
            'last_name',
            'password',
            'password2',
        )
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError({"password": "Password fields didn't match."})

        return attrs

    def create(self, validated_data):
        user = User.objects.create(
            username=validated_data['username'],
            email=validated_data['email'],
            first_name=validated_data['first_name'],
            last_name=validated_data['last_name']
        )

        user.set_password(validated_data['password'])
        user.save()

        return user


class LogoutSerializer(serializers.Serializer):
    refresh = serializers.CharField(max_length=1000, required=True)

    class Meta:
        fields = (
            'refresh',
        )

    def validate(self, attrs):
        if 'refresh' not in attrs.keys():
            raise ValidationError('refresh token is not found')

        return attrs
