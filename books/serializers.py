from rest_framework import serializers
from .models import *

class AuthorSerializer(serializers.ModelSerializer):
	authors = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = Author
		fields = ['id', 'name', 'last_name']

class BookSerializer(serializers.ModelSerializer):
	# author = AuthorSerializer()
	authors = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = Book
		fields = ['id', 'name', 'publish_year', 'pages', 'price', 'created_at', 'updated_at', 'authors']
	

class BooksAuthorsSerializer(serializers.ModelSerializer):
	authors = serializers.StringRelatedField(many=True, read_only=True)
	class Meta:
		model = BooksAuthors
		fields = ['id', 'book', 'author']