
from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.CharField(max_length=100, unique=True)  # 사용자 ID를 위한 칼럼
    name = models.CharField(max_length=100)
    passwd = models.CharField(max_length=100)

    class Meta:
        db_table = 'user'  # 테이블 이름을 'user'로 설정

    def __str__(self):
        return self.name
