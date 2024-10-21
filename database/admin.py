from django.contrib import admin
from .models import UserProfile

@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('email_id', 'nickname')  # 관리자 페이지에서 표시할 필드
    search_fields = ('enail_id', 'nickname')  # 검색 필드 추가
