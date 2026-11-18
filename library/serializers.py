from rest_framework import serializers
from library.models import Author,Book
class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields=["id","title"]
class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        books=BookSerializer(many=True,read_only=True)
        model=Author
        fields=["id","name","books"]