from django.db import models
from django.contrib.auth.models import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin
from django.contrib.auth.models import BaseUserManager

# Create your models here.
class UserProfileManager(BaseUserManager):
    """ Helps django works with our custom user model """

    def create_user(self, email, name, password=None):
        """ Creates a new user profile object """
        # check the email address
        if not email:
            raise ValueError('Users must have an active email address.')

        # normalize the email
        email = self.normalize_email(email)
        # create the new user
        user = self.model(email=email, name=name)

        # set the user encrypted password
        user.set_password(password)
        # save the user
        user.save(using=self._db)

        return user


    def create_superuser(self, email, name, password):
        """ Creates and saves a new superuser profile object """

        # create a normal user with the given parameters
        user = self.create_user(email, name, password)

        # set is_superuser and is_staff to True
        user.is_superuser = True
        user.is_staff = True

        # save the new user
        user.save(using=self._db)

        return user




class UserProfile(AbstractBaseUser, PermissionsMixin):
    """Represent a 'user profile' inside our system """

    # class fields
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)

    # object manager
    objects = UserProfileManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    # helper functions
    def get_full_name(self):
        """Used to get a users full name """
        return self.name

    def get_short_name(self):
        """Used to get a users short name """
        return self.name

    def __str__(self):
        """ Used to convert the object to a string """
        return self.email
