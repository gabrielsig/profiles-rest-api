from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter
from . import views

# create the router for the ViewSets
router = DefaultRouter()
# register the viewsets urls to the router
router.register('profile', views.UserProfileViewSet)
router.register('login', views.LoginViewSet, base_name='login')


urlpatterns = [
    url(r'', include(router.urls), name='test viewset'),
]
