from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'password', 'url']
        extra_kwargs = {'password': {'write_only': True}}
    
    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'username', 'name', 'price', 'reference')
        
class ProductByUserSerializer(serializers.HyperlinkedModelSerializer):
    #Serialize username like current user
    username = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )    
    class Meta:
        model = Product
        fields = ('id', 'username', 'name', 'price', 'reference')