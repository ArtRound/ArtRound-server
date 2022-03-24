from django.contrib import admin
from .models import Answer
from .models import Review, Image
from .models import Question
from .models import Notice
from .models import Favorites
from .models import User

from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken

# Image 클래스를 inline으로 나타낸다.
class ImageInline(admin.TabularInline):
    model = Image

# Review 클래스는 해당하는 Image 객체를 리스트로 관리하는 한다. 
class ReviewAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]

admin.site.register(Review, ReviewAdmin)
admin.site.register(Question)
admin.site.register(Notice)
admin.site.register(Favorites)
admin.site.register(Answer)
admin.site.register(User)

class CustomOutstandingTokenAdmin(OutstandingTokenAdmin):
    def has_delete_permission(self, *args, **kwargs):
        return True


admin.site.unregister(OutstandingToken)
# Register your models here.
