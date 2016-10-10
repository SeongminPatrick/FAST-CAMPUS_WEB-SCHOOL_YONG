#Django_document_queryset

```python
class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):              # __unicode__ on Python 2
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField()
    authors = models.ManyToManyField(Author)
    n_comments = models.IntegerField()
    n_pingbacks = models.IntegerField()
    rating = models.IntegerField()

    def __str__(self):              # __unicode__ on Python 2
        return self.headline
```

#### Create objects
- Blog.objects.create(name="my blog", tagline="hello")
- Entry.objects.create(authors=a1) 는 사용할 수 없다. Mayn to Many가 포함된 클래스의 객체를 만들기위해서는 객체를 먼저 만든 뒤 다른 객체를 더해 주어야한다.
>joe = Author.objects.create(name="Joe")
> entry.authors.add(joe)

#### Queryset
 - Queryset은 chaining이 가능하다.
 - DB접속은 실제 연산이 수행될때 이루어진다(print(q))
 - objects.get() 한개의 객체만 받을 수 있고 한개 이상일 경우 MultipleObjectsReturned 에러를 발생 시킨고 값이 없을 경우 Does not exist에러를 발생 시킨다.
- objects.filter() 조건에 맞는 queryset을 리턴하고 값이 없어도 에러를 일으키지 않는다.

#### clear() vs delete()
- entry.authors.clear() : clear()는 many_to_many의 관계만 지워지고
- entry.authors.all().delete() : delete()는 객체를 지우므로 객체와 관계 모두 지워진다.

#### Queryset AND OR 연산

- AND연산은 ","로 이루어 진다. ex) Blog.objects.filter(entry__headline__contains='Lennon', entry__pub_date__year=2008)
- OR 연산은 Q함수를 import하여 "|" 연산자를 이용하여 수행할 수 있다. ex) 
```python
from django.db.models import Q

	Poll.objects.get(
	    Q(question__startswith='Who'),
	    Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6))
	)
```
 - Q함수를 이용하지 않는 부분은 **kwarg에 해당하기 때문에 제일 마직막에 적어 주어야 한다. ex)
 
		Poll.objects.get(
		   Q(pub_date=date(2005, 5, 2)) | Q(pub_date=date(2005, 5, 6)),
		   question__startswith='Who',
		)
#### Copy instance

```python
blog = Blog(name='My blog', tagline='Blogging is easy')
blog.save() # blog.pk == 1

blog.pk = None
blog.save() # blog.pk == 2
```	 
- pk 값에 None을 넣어주면 pk는 변할 수 없는 요소이기 때문에 pk값을 1증가 시켜 똑같은 객체를 생성해 준다.

