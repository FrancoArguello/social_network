from django.contrib import admin
from .models import User, Profile


#esto nos sirve para
admin.site.register(User)
admin.site.register(Profile)