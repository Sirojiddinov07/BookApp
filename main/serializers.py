from rest_framework import serializers
from django.contrib.auth.models import User
from .models import *

class SubcategorySerializer(serializers.Serializer):
    class Meta:
        model = Subcategory
        fields = '__all__'




class CategorySerializer(serializers.Serializer):
    class Meta:
        model = Category
        fields = '__all__'



class ImageSerializer(serializers.Serializer):
    class Meta:
        model = Image
        fields = '__all__'



class AudioSerializer(serializers.Serializer):
    class Meta:
        model = Audio
        fields = '__all__'




class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'




class BooksSerializer(serializers.ModelSerializer):
    reviews = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Books
        fields = '__all__'

    def get_reviews(self, obj):
        reviews = obj.review_set.all()
        serializer = ReviewSerializer(reviews, many=True)
        return serializer.data
