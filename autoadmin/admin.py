from django.contrib import admin
from .models import Account, Question, Answer


admin.site.register(Account)
admin.site.register(Question)
admin.site.register(Answer)