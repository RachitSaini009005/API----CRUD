from django.contrib import admin
from django.urls import path, include  # Import include function
from django.views.generic import RedirectView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', RedirectView.as_view(pattern_name='product-list-create', permanent=False)),  # It is use to Redirect root URL to products/
    path('', include('App.urls')),  # Include the URL patterns defined in the 'App' app

]
