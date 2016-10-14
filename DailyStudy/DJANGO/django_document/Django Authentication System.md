# Using the Django authentication system

### Authentication vs Authorization

###User objects
인증 시스템의 핵심 오브젝트로 장고에서는 인증을 위해 오직 Object 클래스 만사용합니다. 'superuseres'나 'staff'또한 특별한 속성을 가지고 있는 User 클래스 입니다. 주요속성은 다음과 같습니다.
- username
- password
- email
- first_name
- last_name

### Create users
```python
>>> from django.contrib.auth.models import User
>>> user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')

```
### Session and Cookie
사용자가 아이디와 비밀번호를 가지고 서버에 접속하면 서버에서는 그 사용자에 해당하는 세션값을 생성하고 돌려줍니다. 그 값을 받은 사용자는 그 값을 쿠키에 저장하여 가지고 있다가 사이트에서 페이지를 이동하는 등의 활동을 할때 요청값과 함께 보냅니다. 서버에서는 사용자가 보낸 세션값을 통해 인증을하며 사용자 권한에 해당하는 리턴 값을 돌려줍니다.

### Authenticating users
autenticate()는 인증을 위해 기본적으로 username과 password를 매개변수로 받습니다. 매개변수로 전달되 값들은  authentication backend의 값들과 비교된 후 유효하면 User객체를 리턴하고 유효하지 않거나 PermissionDenied가 발생하면 None 값을 리턴 합니다.

### Permissions and Authorization
장고에서는 사용자 개인이나 사용자 그룹을 대상으로 자격을 할당 할 수 있습니다. form이나 object에 대한 add, change, delete등의 기능에 따라 자격을 할당 할 수 있습니다. 또한 User 오브젝트는 groups과 user_psermissions라는 2개의 many-to-many 필드를 가지고 있습니다.

### How to log a user in
authenticating이 이루어지면 다음은 session에 id값을 등록해야 하는데 이때 사용되는 함수가 login()이다. login()은 HttpRequest와 User객체를 매개변수로 받고 사용자의 아이디를 session에 등록한다.
