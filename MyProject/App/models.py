from django.db import models  # Importing the models module from Django to define database models.

# Define custom user model with additional fields
class CustomUser(models.Model):  # Creating a custom user model.
    username = models.CharField(max_length=50, unique=True)  # It is used for storing the username with max length of 50 characters and must be unique
                                                              
    email = models.EmailField(unique=True)  # This is use for storing email address and  ensuring uniqueness.
                                            
    password = models.CharField(max_length=20)  # This Fields is storing the password with a max length of 20 characters.
                                                   
    is_approved = models.BooleanField(default=False)  # It is use to indicate whether the user has been approved by an admin.

# Define model for products
class Product(models.Model):  # Creating a model to represent products.
    name = models.CharField(max_length=50)  # This Field is used for storing the name of the product with max length 50 characters

    description = models.TextField()  # This Field is storing the description of the product, which can hold a large amount of text.

    price = models.DecimalField(max_digits=6, decimal_places=2)  # This Field is for  storing the price of the product as a decimal number with a maximum of 6 digits and 2 decimal places.
    # owner = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  #This Field is  representing a relationship between products and users, where each product belongs to a user.

    def __str__(self):  # Method to return a string representation of the product object.
        return self.name  # Returning the name of the product as its string representation.
