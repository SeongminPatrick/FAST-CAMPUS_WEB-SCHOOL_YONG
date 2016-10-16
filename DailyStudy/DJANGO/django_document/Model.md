# Django_document_Model2

### 1. Model 상속

```python

class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)


class Student(Person):
    year = models.CharField(max_length=20))
```
- Student 모델이 Person 모델을 상속하는 예제.
- Person 테이블과 Student 테이블이 생성되고, Person 테이블에는 first_name과 last_name이 Student테이블에는  Student 테이블과 Person 테이블을 이어주는 새로운 컬럼과 year이 생성된다. 
- 새로운 컬럼은 외래키와 같은 역할을 한다.
- Student객체를 만드려면 Student.objects.create(first_name="용필", last_name="문", year=4) 다음과 같이 입력한다.
- Meta속성도 자동으로 상속되며 상속된 성질을 다시 돌려주기 위해서는 다시 정의해 주어야한다. ex) ordering = [ ]

### 2. Abstract class
```python

class CommonInfo(models.Model):
    name = models.CharField(max_length=100)
    age = models.PositiveIntegerField()

    class Meta:
        abstract = True

class Student(CommonInfo):
    home_group = models.CharField(max_length=5)
```

- 상속과는 다르게 CommonInfo 테이블은 생성되지 않고 상속받은 Student클래스만 생성된다.
- Student는 name, age, home_group 컬럼을 모두 가지고 있다.
- CommonInfo 객체를 생성하려하면 오류가 발생한다.
- 상속과 마찬가지고 Meta속성도 상속되지만 abstract는 상속되지 않는다.

### 3. Multiple Model 상속
```python
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    ...

class Book(models.Model):
    book_id = models.AutoField(primary_key=True)
    ...

class BookReview(Book, Article):
    pass
```
- 상속과 유사하지만 BookReview테이블에서 pk값을 구분하기 위해 Article과 Book 클래스에서 pk값을 특정 이름으로 지정해 주어야한다.

### 4. Symmetrical 요소
```python
class Person(models.Model):
    name = models.CharField(max_length=100)
    relationships = models.ManyToManyField('self', through='Relationship', 
                                           symmetrical=False, 
                                           related_name='related_to+')

RELATIONSHIP_FOLLOWING = 1
RELATIONSHIP_BLOCKED = 2
RELATIONSHIP_STATUSES = (
    (RELATIONSHIP_FOLLOWING, 'Following'),
    (RELATIONSHIP_BLOCKED, 'Blocked'),
)

class Relationship(models.Model):
    from_person = models.ForeignKey(Person, related_name='from_people')
    to_person = models.ForeignKey(Person, related_name='to_people')
    status = models.IntegerField(choices=RELATIONSHIP_STATUSES)
```
- many to many 관계에서 자기자신과 관계를 갖는 클래스를 생성할때는 symmetrical=False로 해주어야 한다.
- 주로 following과 follower 관계를 나타 낼때 사용된다.

### 5. 상속 vs abstract
- 부모클래스로 부터 참조하여 사용해야할 경우가 있는 경우 상속을 사용하고 자식 모델만 사용할 경우 abstract를 사용

### 6. proxy
- 상속받은 모델과 같은 테이블을 사용하지만 ordering과 같은 Meta 속성이나 다른 함수들을 추가하여 새로운 클래스를 만들어 사용하고 싶을 때 사용한다.


#### DateTimeField
- auto_now_add : 처음 생성될때의 날짜 기록
- auto_add : 생성된 후 저장될때마다 변경

