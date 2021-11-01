from django.core import serializers
from rest_framework import serializers
from .models import Change

class ChangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Change
        fields = ['no','user_id','prev_pwd','new_pwd']
        no = serializers.IntegerField()
        user_id = serializers.CharField(max_length=18)
        prev_pwd = serializers.CharField(max_length=18)
        new_pwd = serializers.CharField(max_length=18)

