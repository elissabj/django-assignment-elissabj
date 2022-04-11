from books import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()

router.register(r'authors', views.AuthorViewSet)
router.register(r'bookauthors', views.BooksAuthorsViewSet)
router.register(r'', views.BookViewSet)

urlpatterns = [
    path('', include(router.urls)),
]