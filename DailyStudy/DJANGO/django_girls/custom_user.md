### Middleware
인증, 보안, 세션값 생성등의 기능들을 제공해주는 부분

### Static
static file에 접근하려고 할 때 

### redirect와 render

redirect 작없을 끝낸다음 담음 역할을 하는 뷰로 넘겨주는것 
view는 자기에 맞는 역할만 해야한다.

render 현재 요청에 정확히 맞는 작업을 해서 template으로 

### user_custumizing

1. password, last_login, is_active의 속성만가지고 있는 AbstractBaseUser클래스를 상속받아서 MyUser를 만든다.
2. USERNAME_FIELD를 인증하고 싶은 필드로 바꾸어 준다
ex) USERNAME_FIELD = 'email'

3. settings file에 AUTH_USER_MODE = 값에 커스터마이증할 모델로 지정해 준다. ex) AUTH_USER_MODE = 'member.MyUser' 
