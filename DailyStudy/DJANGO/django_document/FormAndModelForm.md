##1. The Django Form class
- form클래스는 form이 어떻게 동작하고 나타내는지 정의 합니다. 
- model클래스가 데이터 베이스의 필드에 맵핑되는 것과 유사하게 form클래스의 필터들은 HTML form의 input요소에 맵핑됩니다. 
- form의 필드들은 하나하나 자신의 클래스를 가지고 있고 form데이터와 validation을 다룹니다. 
- form필드들은 사용자의 브라우저에서 HTML "widget"으로 나타나며 각 필드는 기본 widget클래스를 가졌지만 override될 수 있습니다.

##2. Bound and unbound forms
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

###2.1 Form.is_valid()
Form.is_valid()의 주요 역할은 유효성을 검사하는 것입니다. form의 데이터 들이 유효하면 True를 리턴 합니다.


###2.2 SignUp Form Example
```python
class SignUpForm(forms.Form):

    email = forms.EmailField(
        max_length=100,
        widget=forms.EmailInput( #html의 형태를 결정한다.
            attrs={'class': 'form-control'}
        )
    )
    password1 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    password2 = forms.CharField(
        widget=forms.PasswordInput(
            attrs={'class': 'form-control'}
        )
    )
    last_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    first_name = forms.CharField(
        max_length=20,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    )
    nickname = forms.CharField(
        max_length=24,
        widget=forms.TextInput(
            attrs={'class': 'form-control'}
        )
    ) 
```
###2.3 SignUp Form View Example
```python
def signup2(request):
    context = {}
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
        # validation이 통과된 데이터만 cleaned_data에 들어간다.  
            email = form.cleaned_data['email']  # 왜 cleaned_date를 사용하나요?
            password1 = form.cleaned_data['password1']
            password2 = form.cleaned_data['password2']
            last_name = form.cleaned_data['last_name']
            first_name = form.cleaned_data['first_name']
            nickname = form.cleaned_data['nickname']

        if password1 != password2:
            return HttpResponse('패스워드가 서로 다릅니다.')

            user = MyUser.objects.create_user(
                email=email,
                last_name=last_name,
                first_name=first_name,
                nickname=nickname,
                password=password1,
            )
	#회원가입 후 자동으로 login시킨다.
            login(request, user)
            messages.info(request, '회원가입 되었습니다')
            return redirect('blog:post_list')
        else:
            context['form'] = form
    else:
        form = SignUpForm()
        context = {
            'form': form,
        }
    return render(request, 'member/signup2.html', context)

```
##3. Model Form

### 3.1 save() method
- 모든 model form은 save() 함수를 가지고 있다. 이 함수는 데이터가 bound된 form으로 부터 데이터베이스 객체를 만들고 저장합니다. 
- ModelForm은 instance keyword로 model 객체를 받을 수 있습니다.
- save()를 호출시 instance로 받은 객체가 있으면 받은 객체를 업데이트 시키고  없으면  새로운 객체를 생성합니다.
- save()를 commit==False와 함께 호출하면 저장되지않은 객체를 반환 합니다. 이 객체를 추가적이으로 처리한 후 원하는 때에 save함수를 호출하여 저장할 수 있습니다.
-  만약 model field속성에 defaul값이 주어지면 form에서 보이지 않습니다.
```python
>>> from myapp.models import Article
>>> from myapp.forms import ArticleForm

# Create a form instance from POST data.
>>> f = ArticleForm(request.POST)

# Save a new Article object from the form's data.
>>> new_article = f.save()

# Create a form to edit an existing Article, but use
# POST data to populate the form.
>>> a = Article.objects.get(pk=1)
>>> f = ArticleForm(request.POST, instance=a)
>>> f.save()
```

### 3.2 SignUp ModelForm Example
```python
#비밀번호 확인 기능을 가진 custom user model SignUp
class SignupModelForm(forms.ModelForm):
#fields에 지정해 주지 않아도 클래스 변수로 지정되 있으면 form의 요소로 인식된다.
    password1 = forms.CharField( 
        label='Password',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )
    password2 = forms.CharField(
        label='Password confirmation',
        widget=forms.PasswordInput(
            attrs={
                'class': 'form-control',
            }
        )
    )

    class Meta:
        model = MyUser
        fields = (
            'email',
            #fields 안에 지정해서 순서를 변경할 수 있다.
            'password1',
            'password2',
            'last_name',
            'first_name',
            'nickname',
        )
		#validation 및 클래스 설정등을 위해 사용된다.
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'nickname': forms.TextInput(attrs={'class': 'form-control'}),
        }
    # is_valid()가 실행할 때 비밀번호를 체크하기위해 실행된다. "clean_요소()"를 통해 원하는 validation기능을 구현해 줄 수 있다.
    def clean_password2(self): 
        password1 = self.cleaned_data.get('password1')
        password2 = self.cleaned_data.get('password2')
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError(
                self.error_messages['password_mismatch'],
                code='password_mismatch',
            )
        password_validation.validate_password(
            self.cleaned_data['password1'],
            self.instance
        )
#비밀번호를 hashing하는 기능을 구현하기 위해 기존의 save()를 overriding 합니다.
    def save(self, commit=True):
        user = super(SignupModelForm, self).save(commit=False)
        user.set_password(self.cleaned_data['password'])
        user.save()
        return user

```
### 3.3 SignUp ModelForm View Example

```python
def signup3(request):
    context = {}
    if request.method == 'POST':
        form = SignupModelForm(request.POST)
        if form.is_valid():
            user = form.save()

            login(request, user)
            return redirect('blog:post_list')
        context['form'] = form
    else:
        form = SignupModelForm()
        context['form'] = form
    return render(request, 'member/signup2.html', context)
```