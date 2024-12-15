from rest_framework import serializers
from users.models import Profile  # Import the renamed model

class UserSerializer(serializers.ModelSerializer):  # Renamed from ProfileSerializer
    class Meta:
        model = Profile
        fields = ['username', 'email', 'password', 'bio']
        extra_kwargs = {'password': {'write_only': True}}

class UserProfileSerializer(serializers.ModelSerializer):  # Renamed from ProfileDetailsSerializer
    class Meta:
        model = Profile
        fields = ['username', 'email', 'bio']  # Omit password for profile details
