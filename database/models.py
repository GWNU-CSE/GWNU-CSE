from django.db import models
from django.contrib.auth.hashers import make_password, check_password

class UserProfile(models.Model):
    username = models.EmailField(unique=True)  # 이메일 형태의 아이디
    password = models.CharField(max_length=128)  # 비밀번호 해시 저장
    nickname = models.CharField(max_length=50)  # 닉네임
    url = models.CharField(max_length=2048, blank=True, null=True) # URL
    def save(self, *args, **kwargs):
        # 비밀번호 해시 처리
        if not self.pk or 'password' in kwargs:  # 새 객체일 때 또는 비밀번호가 변경될 때
            self.password = make_password(self.password)
        super().save(*args, **kwargs)

    def check_password(self, raw_password):
        """ 주어진 비밀번호가 저장된 해시 비밀번호와 일치하는지 확인 """
        return check_password(raw_password, self.password)
