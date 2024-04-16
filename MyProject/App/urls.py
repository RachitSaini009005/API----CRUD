from django.urls import path  # Import the path function from Django to define URL patterns.
from .views import (  # Import views from the current directory to associate with URL patterns.
    UserCreateView, UserLoginView, ProductCRUDView, UserApprovalView, ProductDeleteView
)

urlpatterns = [
    path('register/', UserCreateView.as_view(), name='user-register'),  # This URL pattern is for user registration view.
    path('login/', UserLoginView.as_view(), name='user-login'),  #  URL pattern for user login .
    path('products/', ProductCRUDView.as_view(), name='product-list-create'),  # URL pattern for product CRUD .
    path('approve/<int:pk>/', UserApprovalView.as_view(), name='user-approval'),  #This URL pattern  is for user approval view.
    path('delete-product/<int:pk>/', ProductDeleteView.as_view(), name='product-delete'),  # URL pattern for product deletion .
]
