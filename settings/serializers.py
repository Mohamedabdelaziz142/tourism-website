from rest_framework import serializers
from property.serailizers import PropertySerializer
from property.models import Category
from property.models import Place
from blog.models import Post
from .models import Settings


class PlaceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Place
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = '__all__'


class HomeSerializer(serializers.Serializer):
    places = PlaceSerializer(many=True)
    category = CategorySerializer(many=True)
    resturant_list = PropertySerializer(many=True)
    hotels_list = PropertySerializer(many=True)
    places_list = PropertySerializer(many=True)
    recent_posts = PostSerializer(many=True)
    users_count = serializers.IntegerField()
    places_count = serializers.IntegerField()
    resturants_count = serializers.IntegerField()
    hotels_count = serializers.IntegerField()

class SettingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Settings
        fields = '__all__'