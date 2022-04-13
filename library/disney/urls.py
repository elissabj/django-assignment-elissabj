from library.disney import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'movies', views.MovieViewSet)
router.register(r'companymovies', views.DisneyCompanyViewSet)
router.register(r'', views.CompanyViewSet)

urlpatterns = [
    path('', include(router.urls)),
]