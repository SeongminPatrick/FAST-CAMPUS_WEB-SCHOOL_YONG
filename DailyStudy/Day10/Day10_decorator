# Day10_Decorator
#### decorator : 함수를 리턴하는 .... 함수

```python
def hello(name):
    print("안녕하세요, 저는" + name + "입니다.")
    
def track_time(func):
    def new_func(*args, **kwargs): # pack!
        start_time = time.time()
        func(*args, **kwargs) # unpack!
        end_time = time.time()
        exec_time = end_time - start_time
        print("Execute Time: {time}".format(time=exec_time))
    return new_func

hello2 = track_time(hello) # hello함수를 받는 track_time함수가 실행되고 실질적으로 hello2함수는 new_func과 같다고 볼 수 있다.
hello2("문용필")
```

```python    
def track_time(func):
    def new_func(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print("Execute Time: {time}".format(time=exec_time))
    return new_func

@track_time # decorator를 통해서 track_time(hello)를 shortcut 형태로 나타낼 수 있다.
def hello(name): 
    print("안녕하세요, 저는" + name + "입니다.")
```

##### 다중 데코레이터
```python
def track_time(func):
    def new_func(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()
        exec_time = end_time - start_time
        print("Execute Time: {time}".format(time=exec_time))
    return new_func

def start_func(func):
    def wapper(*args, **kwargs):
        print ("==== 함수를 실행합니다 ====")
        return func(*args, **kwargs)
    return wapper

def finish_func(func):
    def wapper(*args, **kwargs):
        result = func(*args, **kwargs)
        print ("==== 함수를 종료합니다 ====")
        return result # return값이 wapper함수의 결과값으로 전달
    return wapper

@track_time
@finish_func
@start_func
def hello(name):
    print("안녕하세요, 저는 " + name + " 입니다.")
    
 hello("문용필")
```
	tip) 함수에 가까이 있는 decorator부터 감싸지면서 적용 된다.
	실행 순서 : 1.@start_func 2.@finish_func 3.@track_time
	 
	==== 함수를 실행합니다 ====
	안녕하세요, 저는 문용필 입니다.
	==== 함수를 종료합니다 ====
	Execute Time: 3.218650817871094e-05

