### Redirect(to, *arg, **kwarg )
to 부분에 urlpattern의 name을 넘겨주면 reverse()를 통해 해당하는 view가 실행된다.

### Ctrl + Shift + f 
프로젝트전체에서 단어를 찾는다.

###?P<PK\>
urlpattern에서 매개변수의 이름을 pk로 지정한다.
```python
form = PostForm(request.POST, instance=post)
form2 = PostForm(request.POST, instance=post)
form3 = PostForm(instance=post)

print(form.data) #내용 있음
print(form2.data #내용 있음
print(form3.data) #내용 없음

print(form.is_valid() #True
print(form2.is_valid()) #True
print(form3.is_valid()) #False
``` edit화면에는 나오지만 ```
print(form3.initial) #True
```

### The Django Form class
- form클래스는 form이 어떻게 동작하고 나타내는지 정의 합니다. 
- model클래스가 데이터 베이스의 필드에 맵핑되는 것과 유사하게 form클래스의 필터들은 HTML form의 input요소에 맵핑됩니다. 
- form의 필드들은 하나하나 자신의 클래스를 가지고 있고 form데이터와 validation을 다룹니다. 
- form필드들은 사용자의 브라우저에서 HTML "widget"으로 나타나며 각 필드는 기본 widget클래스를 가졌지만 override될 수 있습니다.

### Bound and unbound forms
```python
data = {'subject': 'hello',
         'message': 'Hi there',
         'sender': 'foo@example.com',
         'cc_myself': True}
 f = ContactForm(data)
``` 	
-  unbound form은 데이터를 가지고 있지 않은 form 입니다. 사용자에게 랜더링되면 빈 값이나 기본 값을 가지고 있는 form을 보여줍니다.
- bound form은 데이터를 가지고 있는 form이고, 데이터를 가지고 있기 때문에 데이터 유효성 검사를 실행할 수 있습니다.
- 데이터가 유효하지 않은  bound form이 랜더링 되면 어떤 데이터가 유효한지 보여주는 inline error를 보여 줄 수 있습니다.

### Form.is_valid()
Form.is_valid()의 주요 역할은 유효성을 검사하는 것입니다. form의 데이터 들이 유효하면 True를 리턴 합니다.
 
