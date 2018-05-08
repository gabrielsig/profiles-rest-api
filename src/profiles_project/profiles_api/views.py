from django.shortcuts import render

from rest_framework import viewsets
from rest_framework import status
from rest_framework import filters
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authentication import TokenAuthentication
from rest_framework.authtoken.serializers import AuthTokenSerializer
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.permissions import IsAuthenticated

from . import serializers
from . import models
from . import permissions

# Create your views here.
class UserProfileViewSet(viewsets.ModelViewSet):
    """ Used to create, reading and updating profiles"""

    # define the serializer class to be used by this view
    serializer_class = serializers.UserProfileSerializer
    # define the queryset so that the view knows how to retreive the models from the database
    queryset = models.UserProfile.objects.all()

    # add the Token authentication class
    authentication_classes = (TokenAuthentication,)

    # define the permission class
    permission_classes = (permissions.UpdateOwnProfile,)

    # define the filter that will be used to search the profiles
    filter_backends = (filters.SearchFilter,)
    # define the fields that will be avaliable to serach the profiles in the db
    search_fields =  ('name', 'email')



class LoginViewSet(viewsets.ViewSet):
    """ Check email and password and returns an auth token """

    # define the serializer class used in this view
    serializer_class = AuthTokenSerializer

    # define the function to be called by HTTP Post request
    def create(self, request):
        """ Use the ObtainAuthToken APIView to validate and create a token"""

        return ObtainAuthToken().post(request)



class UserProfileFeedViewSet(viewsets.ModelViewSet):
    """ Handles crating, reading and updating profile feed items"""

    # define the authentication class
    authentication_classes = (TokenAuthentication,)
    # define the serializer class
    serializer_class = serializers.ProfileFeedItemSerializer
    # define the queryset so that the view knows how to retreive the models from the database
    queryset = models.ProfileFeedItem.objects.all()
    # add the permission classes
    permission_classes = (permissions.PostOwnStatus, IsAuthenticated)
    #permission_classes = (permissions.PostOwnStatus, IsAuthenticatedOrReadOnly)

    # customize the logic that is run whe a new object is created in the viewset
    def perform_create(self, serializer):
        """Sets the user profile on the feed item as the logged in user"""

        serializer.save(user_profile=self.request.user)
