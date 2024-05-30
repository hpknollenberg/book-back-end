from django.contrib import admin
from app_book.models import *

class ProfileAdmin(admin.ModelAdmin):
    pass

My_Models = [Profile, Bookshelf, Book]
admin.site.register(My_Models, ProfileAdmin)
