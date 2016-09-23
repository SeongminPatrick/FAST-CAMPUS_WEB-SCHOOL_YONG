# Day_12_iterator_and_generator

#### Iterator

- 객체가 Iterable 하다
	- \__iter()__함수가 정의 되어 있고 이 함수를 통해 iterator객체를 생성할 수 있다. 
	- Iterable한 객체 : List, Dict, Tuple, Set, String
	- Iterable하다와 Iterator는 같지 않다.
	
- Iterator
	- \__next()__ 함수가 정의 되어있고 이 함수를 수행 시 다음 element가 리턴된다.
	- element가 모두 리턴되면 StopIteration Error를 발생 시킨다.
	
- Iter()함수와 next()함수는 다음과같이 호출 할 수 있다.
```python
animals_iterator = iter(animals)
# animals_iterator = animals.__iter__()

next(animals_iterator)
# animals_iterator.__next__()
```

#### Myrange()로 iterator 이해하기

- 다음과 같이 iterable하면서 iterator인 myrange class를 정의할 수 있다.
```python
class Myrange():
    def __init__(self,n):
        self.i, self.n = 0, n
    
    def __iter__(self): #__iter()___는 iterator를 리턴해야 되기 때문에 iterable하면서 iterator인 자기 자신을 리턴한다.
        return self
    
    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i
        else:
            raise StopIteration
```
- 이렇게 정의된 함수는 list(myrange)를 적용하면 한번은 아무 문제 없이 잘 수행되지만 그 다음 부터는 아무값도 리턴하지 않는다.
- 반면 range(5)로 생성된 객체는 반복적으로 list()를 호출해도 값이 잘 출력된다.

		tip) # range로 만들어진 r은 iterable한 객체이기 때문에 __iter__()함수를 통해 iterator를 생성하고  iterator는 list()함수 안에서 __next__함수를 호출하면서 데이터를 리턴하고 마지막으로 stop에러를 발생시키고 사라진다.
			# 반면에 myr은 자신이 iterable한 객체이면서 iterator기 때문에 __iter()__ 함수를 통해 자기자신을 생성하고 list()함수 안에서 자신의 __next__()함수를 호출하며 데이터를 소모한다. 그렇기 때문에 2번째 list(myr)를 호출하면 아무 데이터도  나오지 않는다.
			
#### Myrange Refactoring
- 다음과 같이 Iterator를 생성해 주는 클래스를 따로 만들어서 myrange를 정상 작동하게 할 수 있다.

```python
class Myrange():
    def __init__(self, n):
        self.n = n
        
    def __iter__(self):
        return MyrangeIterator(self.n)
    
class MyrangeIterator():
    def __init__(self, n):
        self.i, self.n = 0,n
        
    def __next__(self):
        if self.i < self.n:
            self.i += 1
            return self.i
        else:
            raise StopIteration
```
- StopIteration Error가 발생하여도 list나 for를 수행하면 객체가 다시 생성되어 정상 작동한다.


#### Generator

- 함수내의 yield가 포함되면 해당 함수를 Generator라고 부른다.
```python
def myrange_iterator(n):                    # myrange_iterator class
    i = 0
    while i < n:
        yield i                    # return => "yield"
        i += 1
```
- Iterator와 같은 역할을 하지만...
- 값을 반환하여도 상태를 유지한다.
- 데이터가 저장되어 있는 상태에서 요소를 하나씩 추출해내는 Iterator와 달리 Generator는 값이 필요한 시점에만 값을 생성하고 반환한다.
```python
class myrange:   # iterable
    
    def __init__(self, n):
        self.n = n
    
    def __iter__(self):
        def myrange_iterator(n):
            i = 0
            while i < n:
                yield i                    # return => "yield"
                i += 1
                
        return myrange_iterator(self.n)    # generator object

```