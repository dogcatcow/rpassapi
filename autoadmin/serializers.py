from django.core import serializers
from rest_framework import serializers
from .models import Account
from datetime import datetime

class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['no','user_id','prev_pwd','receive_date']
        user_id = serializers.CharField(max_length=18)
        prev_pwd = serializers.CharField(max_length=18)
        receive_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')