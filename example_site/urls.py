from django.urls import path
from example_site.views import index



urlpatterns = [
    path('', index, name="index")
]