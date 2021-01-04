from django.contrib.auth.models import User, Group
from rest_framework import serializers
from .models import Product

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'url', 'email', 'groups']

class GroupSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Group
        fields = ['url', 'name']
        
class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('id', 'username', 'name', 'price', 'reference')
        
class ProductByUserSerializer(serializers.ModelSerializer):
    #Serialize username like current user
    username = serializers.HiddenField(
        default=serializers.CurrentUserDefault()
    )    
    class Meta:
        model = Product
        fields = ('id', 'username', 'name', 'price', 'reference')