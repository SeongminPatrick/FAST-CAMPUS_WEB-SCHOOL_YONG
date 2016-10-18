from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager, User


class YoutubeUserManager(UserManager):
    pass


# 기본 장고 User모델에 필드를 더 추가하고 싶을 때 사용됩니다.
class YoutubeUser(AbstractUser):
    nickname = models.CharField(max_length=24)

    class Meta:
        verbose_name = '사용자'
        verbose_name_plural = '사용자 목록'

    def __str__(self):
        return self.username
