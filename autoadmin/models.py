from django.db import models


class Account(models.Model):
    no = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=18)
    prev_pwd = models.CharField(max_length=18)
    receive_date = models.DateTimeField(auto_now_add=True)