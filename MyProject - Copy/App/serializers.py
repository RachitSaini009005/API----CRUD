from rest_framework import serializers  # Importing serializers module from Django Rest Framework for converting complex data types to native Python data types.
from .models import CustomUser, Product  # Importing CustomUser and Product models from the current directory.

# Serializer for custom user model
class UserSerializer(serializers.ModelSerializer):  # For the CustomUser model we are Creating a serializer class.
    class Meta:  # Meta class is used for  providing  additional information about the serializer.
        model = CustomUser  # It is used for Specifying the model to be serialized.
        fields = ['id', 'username', 'email', 'is_approved']  # It is used for Specifying which fields of the model should be included in the serialized representation.

# Serializer for product model
class ProductSerializer(serializers.ModelSerializer):  # Creating a serializer class for the Product model.
    class Meta: 
        model = Product  # It is used for Specifying the model to be serialized.
        fields = ['id', 'name', 'description', 'price']   # It is used for Specifying which fields of the model should be included in the serialized representation.
