from django.contrib import admin
from .models import UserProfile, UserURL

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'nickname')
    search_fields = ('username', 'nickname')

class UserURLAdmin(admin.ModelAdmin):
    list_display = ('user_profile', 'url')
    search_fields = ('url',)

admin.site.register(UserProfile, UserProfileAdmin)
admin.site.register(UserURL, UserURLAdmin)

