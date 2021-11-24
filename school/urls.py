from django.urls import path
from django.urls import path
from  .views import sample_url

urlpatterns = [
    path('sample/',sample_url),
]