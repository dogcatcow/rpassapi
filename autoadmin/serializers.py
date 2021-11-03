# from django.core import serializers
from rest_framework import serializers
from .models import Account, Question
from datetime import datetime


class AccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ['no', 'user_id', 'prev_pwd', 'create_date']
        user_id = serializers.CharField(max_length=18)
        prev_pwd = serializers.CharField(max_length=18)
        create_date = datetime.now().strftime('%Y-%m-%d %H:%M:%S')


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ['subject', 'content', 'create_date']
        subject = serializers.CharField(max_length=30)
        content = serializers.CharField(max_length=255)
