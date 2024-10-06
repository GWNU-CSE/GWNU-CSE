
from django.contrib import admin
from .models import UserProfile

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('username', 'nickname', 'image', 'video_file')  # 표시할 필드
    search_fields = ('username', 'nickname')  # 검색할 수 있는 필드


admin.site.register(UserProfile, UserProfileAdmin)