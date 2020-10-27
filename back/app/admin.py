from django.contrib import admin
from .models import *
from django.contrib.auth.models import User

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Project)
admin.site.register(Field)
admin.site.register(Photo)
admin.site.register(Test)
admin.site.register(Comment)
admin.site.register(RepondreComment)
