from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import serializers
from . import models

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Used to create, reading and updating profiles"""

    # define the serializer class to be used by this view
    serializer_class = serializers.UserProfileSerializer
    # define the queryset so that the view knows how to retreive the models from the database
    queryset = models.UserProfile.objects.all()
    
