from books import views
from rest_framework import routers
from django.urls import path, include

router = routers.DefaultRouter()
router.register(r'books', views.BookViewSet)
router.register(r'authors', views.AuthorViewSet)
router.register(r'bookauthors', views.BooksAuthorsViewSet)

urlpatterns = [
    path('', include(router.urls)),
]