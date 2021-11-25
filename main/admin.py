from django.contrib import admin
from .models import Review
from .models import Question
from .models import Notice
from .models import Favorites

admin.site.register(Review)
admin.site.register(Question)
admin.site.register(Notice)
admin.site.register(Favorites)
# Register your models here.
