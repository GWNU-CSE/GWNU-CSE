from django.db import models
from django.contrib.auth.hashers import make_password
from django.core.validators import URLValidator
from django.core.exceptions import ValidationError

class UserProfile(models.Model):
    email_id = models.EmailField(unique=True)  # 이메일 형태의 아이디
    password = models.CharField(max_length=128)  # 비밀번호 해시 저장
    nickname = models.CharField(max_length=50)  # 닉네임
    urls = models.JSONField(default=list, blank=True)  # URL 리스트 저장

    def __str__(self):
        return self.email_id

    def save(self, *args, **kwargs):
        # 비밀번호 해시 처리
        if not self.pk or not self.password.startswith('pbkdf2_'):  # 새 객체이거나 비밀번호가 해시되지 않은 경우
            self.password = make_password(self.password)
        super().save(*args, **kwargs)
