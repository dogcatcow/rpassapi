from django.urls import path
from .views import index, submit_account, change_account

urlpatterns = [
    path('', index),
    path('submit_account/', submit_account),
    path('change_account/', change_account)
]
