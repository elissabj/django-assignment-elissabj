from animals import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'environments', views.EnvironmentViewSet)
router.register(r'animalenviron', views.AnimalEnviViewSet)
router.register(r'', views.AnimalViewSet)

urlpatterns = [
    path('', include(router.urls)),
]