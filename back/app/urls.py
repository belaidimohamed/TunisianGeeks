from django.urls import path ,include
from rest_framework import routers
from .views import *
from django.views.decorators.csrf import csrf_exempt


router = routers.DefaultRouter()
router.register('users',UserViewSet)
router.register('field',FieldViewSet)
router.register('project',ProjectViewSet)
router.register('profile',ProfileViewSet)
router.register('photo',PhotoViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('api/token/', CustomAuthToken.as_view()),
]
 