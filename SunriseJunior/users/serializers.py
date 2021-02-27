from rest_framework import serializers
from .models import User


class UserCreateSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})
    repeat_password = serializers.CharField(style={"input_type": "password"}, write_only=True, label="Confirm password")

    class Meta:
        model = User
        fields = ('email', 'first_name', 'last_name', 'password', 'repeat_password')
        extra_kwargs = {"password": {"write_only": True}}

    def validate(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        repeat_password = validated_data["repeat_password"]

        if (email and User.objects.filter(email=email).exists()
                and User.objects.filter(email=email).exists()):
            raise serializers.ValidationError(
                {"email": "Email must be unique."})
        if password != repeat_password:
            raise serializers.ValidationError(
                {"password": "The two passwords differ."})

        return validated_data

    def create(self, validated_data):
        email = validated_data["email"]
        password = validated_data["password"]
        first_name = validated_data["first_name"]
        last_name = validated_data["last_name"]
        user = User.objects.create(email=email, password=password, first_name=first_name, last_name=last_name)
        user.is_active = False
        user.save()
        return user


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('first_name', 'last_name')


class UserSignInSerializer(serializers.ModelSerializer):
    email = serializers.CharField(write_only=True, required=True)
    password = serializers.CharField(write_only=True, required=True, style={"input_type": "password"})

    class Meta:
        model = User
        fields = ('email', 'password')

