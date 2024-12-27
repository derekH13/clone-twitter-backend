from rest_framework import serializers
from ..models import Profile


class ProfileSerializer(serializers.ModelSerializer):
    profile_connections = serializers.PrimaryKeyRelatedField(
        many=True, read_only=True)

    class Meta:
        model = Profile
        fields = ['id', 'user', 'bio', 'avatar', 'profile_connections']
