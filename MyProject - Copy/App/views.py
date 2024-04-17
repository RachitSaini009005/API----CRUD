from rest_framework import generics, permissions  # Import necessary modules for views and permissions from Django Rest Framework.
from .models import CustomUser, Product  # Import CustomUser and Product models from the current directory.
from .serializers import UserSerializer, ProductSerializer  # Import serializers for CustomUser and Product models.

# View for user registration
class UserCreateView(generics.CreateAPIView):  # This view handles user registration. It allows users to create a new account.
    queryset = CustomUser.objects.all()  # Fetch all CustomUser objects from the database.
    serializer_class = UserSerializer  # Use the UserSerializer for serializing and deserializing CustomUser objects.

# View for user login
class UserLoginView(generics.RetrieveAPIView):  # This view handles user login. It retrieves user details for login purposes.
    queryset = CustomUser.objects.all()  # Fetch all CustomUser objects from the database.
    serializer_class = UserSerializer  # Use the UserSerializer for serializing and deserializing CustomUser objects.

# View for product CRUD operations
class ProductCRUDView(generics.ListCreateAPIView):  # This view handles CRUD operations for products. It allows listing and creating products.
    queryset = Product.objects.all()  # Fetch all Product objects from the database.
    serializer_class = ProductSerializer  # Use the ProductSerializer for serializing and deserializing Product objects.
    permission_classes = [permissions.IsAuthenticated]  # Only authenticated users can access this view.

# View for admin user to approve or disapprove accounts
class UserApprovalView(generics.UpdateAPIView):  # This view handles account approval by admin users. It updates the approval status of user accounts.
    queryset = CustomUser.objects.all()  # Fetch all CustomUser objects from the database.
    serializer_class = UserSerializer  # Use the UserSerializer for serializing and deserializing CustomUser objects.
    permission_classes = [permissions.IsAdminUser]  # Only admin users can access this view.

# View for admin user to delete any user's product
class ProductDeleteView(generics.DestroyAPIView):  # This view allows admin users to delete any user's product. It handles product deletion.
    queryset = Product.objects.all()  # Fetch all Product objects from the database.
    serializer_class = ProductSerializer  # Use the ProductSerializer for serializing and deserializing Product objects.
    permission_classes = [permissions.IsAdminUser]  # Only admin users can access this view.
