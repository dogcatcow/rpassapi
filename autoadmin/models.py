from django.db import models
from datetime import datetime

class Account(models.Model):
    no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=18)
    prev_pwd = models.CharField(max_length=18)
    create_date = models.DateTimeField(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

class Question(models.Model):
    subject = models.CharField(max_length=200)
    content = models.TextField()
    create_date = models.DateTimeField(default=datetime.now().strftime('%Y-%m-%d %H:%M:%S'))

    def __str__(self):
        return self.subject

class Answer(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    content = models.TextField()
    create_date = models.DateTimeField()