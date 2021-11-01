from django.urls import path
from .views import index, change, change_pw, fetch
# from . import views

urlpatterns = [
    path('', index),
    path('change/', change),
    path('change_pw/', change_pw),
    path('fetch/', fetch)
]
