from django.urls import path
from .views import *

urlpatterns = [
    path('download', downloadTikTok, name="downloadTikTok"),
]


