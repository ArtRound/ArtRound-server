from django.contrib import admin
from .models import Review
from .models import Question
from .models import Notice

admin.site.register(Review)
admin.site.register(Question)
admin.site.register(Notice)
# Register your models here.
