from django.db import models
from django.contrib.auth.hashers import make_password

class UserProfile(models.Model):
    username = models.CharField(max_length=150, unique=True)
    password = models.CharField(max_length=128)
    nickname = models.CharField(max_length=50)
    website_url = models.URLField(blank=True, null=True)

    def save(self, *args, **kwargs):
        # 비밀번호 해시 처리
        if not self.pk:  # 새 객체일 때만 비밀번호 해시 처리
            self.password = make_password(self.password)
        super().save(*args, **kwargs)