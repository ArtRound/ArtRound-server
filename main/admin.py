from django.contrib import admin
from .models import Answer, Review
from .models import Question
from .models import Notice
from .models import Favorites
from .models import User

from rest_framework_simplejwt.token_blacklist.admin import OutstandingTokenAdmin
from rest_framework_simplejwt.token_blacklist.models import OutstandingToken


admin.site.register(Review)
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
