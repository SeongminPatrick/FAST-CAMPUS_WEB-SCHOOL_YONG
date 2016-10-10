#Day11_Class

#### Polymorphsim - Parametic Polymorhism (Overloading)

```python
class Animal:

    def __init__(self, type, weight):
        self.type = type
        self.weight = weight

    def eat(self, *args):
        print(args)
        if not args:
            print("먹이를 먹습니다.")
        for arg in args:
            print("/n".join([
                "{feed}을/를 먹습니다.".format(feed=arg)
            ]))

    def swim(self):
        print("헤엄을 친다." if self.type == "fish" else "물에 빠진다.")

d4 = Animal("dog", 4)
d5 = Animal("dog", 5)
d6 = Animal("cat", 6)
c3 = Animal("cat", 3)
f10 = Animal("fish", 10)

d4.eat("소시지", "감자", "햄")
d5.eat()
f10.swim()
d4.swim()
```

	결과 값:
	('소시지', '감자', '햄')
	소시지을/를 먹습니다.
	감자을/를 먹습니다.
	햄을/를 먹습니다.
	()
	먹이를 먹습니다.
	헤엄을 친다.
	물에 빠진다.
	
- *args를 사용하면 여러개의 매개변수를 튜플로 pack하여 받을 수 있다.
- 튜플로 pack된 매개변수들에 따라 함수안에서 다른 기능들을 구현 해 줄 수 있다.

#### instance_method, class_method, static_method


```python
class Awesome():
    def __init__(self, name):
        self.__name = name

    @property #.name만 입력해서 함수로 처리된다.
    def name(self):
        print("Getter Called")
        return self.__name # __ 이 붙으면 내부에서 사용된다는 의미이다

    """instance Method"""
    def my_instance_method(self):
        return self

    """Class Method"""
    @classmethod
    def my_class_method(cls):
        return cls # class를 받아 class를 반환한다

    """ Static Method """
    # argument를 받지 않는다
    # Mthode만 있고 속성은 없다
    @staticmethod
    def my_static_method():
        return "static"

awesome = Awesome("name")
print(awesome.name)
# awesome.name = "dobestan" # error: 외부에서 접근할 수 없음
print(Awesome.my_class_method())
print(awesome.my_static_method())
print(Awesome.my_static_method())
``` 	
	결과 값:
	Getter Called
	name
	<class '__main__.Awesome'>
	static
	static
	
- Class method
	- Class를 통해서만 호출 가능하다.
	- instance매소드가 호출시 instance를 첫번째 인자로 넘겨 주듯이 첫 번째 인자로 class를 넘겨 준다.
	
	
```python
# login_required   유저가 로그인 되었는지              @login_required
# is_admin         유저가 관리자인지                  @is_admin


# User Class :: username, is_admin


# Request    :: user instance ( user O => 로그인 O ; user X => 로그인 X ), url(string)
#    request = Request()
#    request.user 
#   
# Response   :: body(string)


class User:
    
    def __init__(self, name, is_admin=False):
        self.name = name
        self.is_admin = is_admin
        

dobestan = User("dobestan")
admin_user = User("admin", is_admin=True)


class Request:
    
    def __init__(self, url, user=None):
        self.url = url
        self.user = user
        

class Response:
    
    def __init__(self, body):
        self.body = body
        
    def __repr__(self):
        return "Response :: {body}".format(body=self.body)
        
 def mypage(request):                            # decorator :: login_required !!!
    return Response("성공적으로 MyPage 에 접속했습니다.")
    
request = Request("/mypage/","dobestan")
mypage(request)

def login_required(func):
    def wrapper(request, *args, **kwargs):
        if request.user:
            response = func(request, *args, **kwargs)
        else:
            response = Response("로그인이 필요합니다.")
        return response
    return wrapper
    
@login_required
def mypage(request):                            # decorator :: login_required !!!
    return Response("성공적으로 MyPage 에 접속했습니다.")
    
def admin(request):                            # decorator :: login_required !!!
    return Response("성공적으로 Admin 에 접속했습니다.")
    
def is_admin(func):
    def wrapper(request, *args, **kwargs):
        if request.user and request.user.is_admin:
            response = func(request, *args, **kwargs)
        else:
            response = Response("관리자 권한이 필요합니다.")
        return response
    return wrapper


@is_admin                 # "로그인이 필요합니다." user => "관리자 권한이 필요합니다."
@login_required
def admin(request):                            # decorator :: login_required !!!
    return Response("성공적으로 Admin 에 접속했습니다.")
    
request = Request("/admin/")
admin(request)                          # 로그인이 필요합니다.
                                        # 권한 Class, Response(권한...)
                                        
request = Request("/admin/", user=dobestan)
admin(request)

request = Request("/admin/", user=admin_user)
admin(request)
```	