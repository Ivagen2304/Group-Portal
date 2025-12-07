from django.contrib import admin
from .models import Question,Answer, Category

admin.site.register(Category)
admin.site.register(Question)
from .models import Answer
