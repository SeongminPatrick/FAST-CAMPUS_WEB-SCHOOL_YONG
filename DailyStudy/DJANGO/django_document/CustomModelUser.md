##AbstractBaseUser
Costom User Model을 구현하기 위한 가장 쉬운 방법 입니다.  AbstractBaseUser는 해쉬 비밀번호, tokenized password reset등의 핵심 기능을 제공합니다. 필드로는 password, lastlogin, is_active를 가지고 있습니다.


##BaseUserManager
Model Manager를 customizing하기 위해서 상속받는 Manager class. User Model을 customizing하면 그에 사용되는 manager도 customizing 해주어야 합니다. customizing을 위해서는 다음 2개의 함수를 구현 해야한다.
#### create_user(*username_field*, password=None, **other_fields)
유저를 생성할 때 사용되는 함수로 USERNAME_FIELD와 REQUIRED_FIELDS에 설정된 값들을 매개변수로 받아야 합니다. 비밀번호를 지정하지 않으면 None 값이 들어갑니다.
```python
def create_user(self, email, date_of_birth, password=None):
    # create user here
    ...
```
#### create_superuser(*username_field*, password, **other_fields)
 슈퍼 유저를 생성할 때 사용되는 함수로 USERNAME_FIELD와 REQUIRED_FIELDS에 설정된 값들을 매개변수로 받아야 합니다.
```python
 def create_superuser(self, email, date_of_birth, password):
    # create superuser here...
```
##AbstractUser
##PermissionsMixin
User Model의 승인 기능들을 쉽게 추가하기 위해 장고는 PermissionMixin 클래스를 제공합니다. 이 추상 모델은 장고의 permission model을 지원하기 위한 메소드나 데이터 베이스 필드를 제공합니다.

#### is_superuser
is_superuser가 True이면 관리자의 모든 권한을 승인 받습니다.

## Extending the existing User model
기존의 유저 모델을 확장하기 위해서는 2가지 방법이 있습니다.
1. 기존 User 데이터를 변경하지 않고 Manager 및 Method의 기능만 바꾼다면 -> Proxy
2. 기존 User 데이터에 다른 요소를 추가하고 싶다면 OneToOneField

## Substituting a custom User model
Username을 사용하는 장고의 인증 시스템은 이메일을 인증 수단으로 사용하고 싶을 경우 적절치 않을 수 있습니다. 이럴 경우를 위해 장고는 인증 시스템을 customizing하는 방법을 제공합니다.  settings file에서 AUTH_USER_MODEL에 설정해 줌으로 써 Custom User Model을 사용할 수 있습니다.
```pyhon
AUTH_USER_MODEL = 'myapp.MyUser'
```
> AUTH_USER_MODEL을 바꾸는 것은 치명적인 데이터 베이스 구조 변화를 이르킬 수 있습니다. Foreign Key 나 Many To Many 관계에 영향을 미칠 수도 있고 makemigration이 재대로 동작하지 않을수도 있습니다. 이러한 상황을 방지 하기 위해서는 다른 테이블을 migrate하기전에 AUTH_USER_MODEL 설정을 해주세요!(AUTH_USER_MODEL은 첫번째 migration에서 실행되도록 하는 것이 좋습니다.)

#### get_user_model()
User 모델을 direct로 참조하는 대신 get_user_model()를 이용할 수 있습니다. 이함수는 Custom User Model이 설정되어있으면 Custom User Model을 그렇지 않으면 장고의 User 모델을 리턴 합니다. Custom User Model의 Foreign key 설정을 위해선 다음과 같이 settings file에서 직접 지정해 줍니다.

```python
from django.conf import settings
from django.db import models

class Article(models.Model):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
```

### Specifying a Custom User model
장고는 Custom User model 사용을 위해 다음과 같은 요구를 합니다.
1. 장고의 authentication backend를 사용하기 위해서는 Custom User Model은 고유한 식별자를 가지고 있어야합니다. 이것은 username이나 email 또는 고유한 다른 필드가 될 수 있습니다.
2.  유저를 나타내기위한 short, long 형식이 존재해야합니다.  가장 흔한 방법은 short 형식으로는 사용자의 이름, long 형식으로는 사용자의 full name을 사용하는 것 입니다. 하지만 원한다면 같은 값을 리턴시켜도 상관 없습니다.

#### USERNAME_FIELD
식별자로 사용될 필드를 지정합니다. 보통은 username을 사용하지만 email 또는 고유한 어떤 식별자도 될 수 있습니다.
```python
class MyUser(AbstractBaseUser):
    identifier = models.CharField(max_length=40, unique=True)
    ...
    USERNAME_FIELD = 'identifier'

```
#### REQUIRED_FIELDS
createsuperuser를 통해 superuser를 만들때 들어가는 field들을 REQUIRED_FIELDS에 설정해 주어야 한다. createsuperuser를 실행하면 다음 요소값들을  입력하라고 요구합니다. REQUIRED_FIELDS는 admin에서 user를 생성하는 등의 다른 경우에는 영향을 미치지 않는다.
```python
class MyUser(AbstractBaseUser):
    ...
    date_of_birth = models.DateField()
    height = models.FloatField()
    ...
    REQUIRED_FIELDS = ['date_of_birth', 'height']
```
> USERNAME_FIELD나 password는 포함하지 않는다.

#### get_full_name()
사용자를 나타내는 long 형식의 식별자. 보통 full name을 나타내지만 어떠한 string 식별자도 가능하다.

#### get_short_name()
사용자를 나타내는 short 형식의 식별자. 보통 full name을 나타내지만 어떠한 string 식별자도 가능하다. get_full_name()과 같은 값을 리턴해도 상관 없다.

#### set_password(raw_password)
주어진 사용자의 raw_password를 저장한다. password hashing을 다룬다.

