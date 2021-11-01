from django.db import models


class Change(models.Model):
    no = models.IntegerField()
    user_id = models.CharField(max_length=18)
    prev_pwd = models.CharField(max_length=18)
    new_pwd = models.CharField(max_length=18)