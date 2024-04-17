# Importing necessary module to register models with Django admin
from django.contrib import admin

# Importing CustomUser and Product models from the current directory
from .models import CustomUser, Product

# Register CustomUser model with the admin site
@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    # It is use to Specify which fields should be shown in the list view for CustomUser in the Django admin interface.
    list_display = ['username', 'email', 'is_approved']
    
    
    # it Allows administrators to filter CustomUser records in the Django admin interface based on the 'is_approved' field."
    list_filter = ['is_approved']
    
    # It is used to Enable administrators to search for CustomUser records in the Django admin interface using their usernames and email addresses.
    search_fields = ['username', 'email']

# Let Django's admin interface handle the Product model.
@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    # "Define the fields that should be displayed in the admin list view for the Product model. These fields will be visible when viewing the list of products in the Django admin interface."
    list_display = ['name', 'description', 'price']
    
    # It Enable's search functionality in the admin list view for Product based on 'name' and 'description' fields
    search_fields = ['name', 'description']
