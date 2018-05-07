from rest_framework import serializers
from . import models


class UserProfileSerializer(serializers.ModelSerializer):
    """ A serializer for the user profile object model """

    # meta class to map serializer's fields with the model fields
    class Meta:
        model = models.UserProfile
        fields = ('id', 'email', 'name', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        """ Creates a new user with the validated data"""

        user = models.UserProfile(
            email = validated_data['email'],
            name = validated_data['name'],
        )

        user.set_password(validated_data['password'])
        user.save()
        return user
