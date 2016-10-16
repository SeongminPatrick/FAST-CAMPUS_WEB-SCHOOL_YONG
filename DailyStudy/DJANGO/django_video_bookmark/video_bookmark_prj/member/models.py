from django.db import models
from django.contrib.auth.models import \
    AbstractBaseUser, BaseUserManager, \
    PermissionsMixin


class MyUserManager(BaseUserManager):

    def create_user(self,
                    email,
                    first_name,
                    last_name,
                    nickname,
                    password):
        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
        )

        user.set_password(password)
        user.save()
        return user

    def create_superuser(self,
                         email,
                         first_name,
                         last_name,
                         nickname,
                         password):

        user = self.model(
            email=email,
            first_name=first_name,
            last_name=last_name,
            nickname=nickname,
        )

        user.set_password(password)
        user.is_staff = True
        user.is_superuser = True
        user.save()
        return user


class MyUser(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=100, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    nickname = models.CharField(max_length=50)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('first_name', 'last_name', 'nickname')

    objects = MyUserManager()

    def get_short_name(self):
        return "{short}".format(short=self.last_name)

    def get_full_name(self):
        return "{short}{long}".format(self.last_name, self.first_name)

