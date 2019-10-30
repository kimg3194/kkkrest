from django.urls import path,include
from rest_framework.routers import DefaultRouter
from userpost import views

router = DefaultRouter()
router.register('userpost', views.UserPostViewSet, base_name = 'UserPost')

urlpatterns = [
  path('', include(router.urls)),
]