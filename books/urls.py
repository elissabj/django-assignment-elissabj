from books import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'books', views.UserViewSet)
router.register(r'groupsBooks', views.GroupViewSet)

urlpatterns = [
    path('', include(router.urls)),
]