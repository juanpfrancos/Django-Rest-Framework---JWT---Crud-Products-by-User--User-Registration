from django.contrib.auth.models import User, Group
from rest_framework import generics, permissions, viewsets
from .serializers import UserSerializer, GroupSerializer, ProductSerializer, ProductByUserSerializer
from .models import Product

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]
class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = [permissions.IsAuthenticated]
    """
    permission_classes = [permissions.IsAuthenticated]
    """
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all().order_by('username')
    serializer_class = ProductSerializer
    #Only the admin can access to all products
    permission_classes = [permissions.IsAdminUser]
    
class ProductsByUser(viewsets.ModelViewSet):
    serializer_class = ProductByUserSerializer
    permission_classes = [permissions.IsAuthenticated]
    #Only return current user products
    def get_queryset(self):
        user = self.request.user
        return Product.objects.filter(username=user)
    
class UserCreate(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
