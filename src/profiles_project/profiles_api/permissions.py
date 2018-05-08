from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow users to edit their own profile and view other profiles"""

    def has_object_permission(self, request, view, object):
        """Check if user has permission to execute the action that is requested"""

        # check if the HTTP method requested by the user is in the safe list
        # if the user is just trying to view a profile (HTTP GET) then we return True
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if the user is updating their own profile
        # verify if the obect that the user is trying to change has the same id of the user that is currently authenticated
        if object.id == request.user.id:
            return True

        # if none of the obove, then return False
        return False



class PostOwnStatus(permissions.BasePermission):
    """Allow users to update their own status"""

    def has_object_permission(self, request, view, object):
        """Check if user has permission to execute the action that is requested"""

        # check if the HTTP method requested by the user is in the safe list
        # if the user is just trying to view the feed (HTTP GET) then we return True
        if request.method in permissions.SAFE_METHODS:
            return True

        # check if the user is updating their own status
        # verify if the obect that the user id of the feed item is the same as the user id that is making the request
        if object.user_profile.id == request.user.id:
            return True

        # if none of the obove, then return False
        return False
