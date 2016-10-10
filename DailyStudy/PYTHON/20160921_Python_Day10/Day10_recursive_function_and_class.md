# DAY10_Recursive_Function_and_Class
#### 피보나치
- for문을 이용한 피보나치 수열 구하기
```python
def for_fibo(n):
    pre, cur = 0, 1
    
    if n < 2:
        return n
    
    for i in range(1,n):
        pre, cur = cur, cur + pre

    return cur
```
- 재귀 함수를 이용한 피보나치 수열
```python
def recursive_fibo(n):
    return n if n < 2 else recursive_fibo(n-1) + recursive_fibo(n-2)
```

#### 팩토리얼
```python
def factorial(n):
    return n if n == 1 else factorial(n-1) * n
```
#### MEMOIZATION
```python
def memoize(func):
    _cache = {}
    def warpper(*args):
        if args in _cache:
            print(_cache)
            return _cache[args]
        else:
            _cache[args] = func(*args) #데코레이션이 적용된 fibo함수가 제귀적으로 실행 된다.
            return _cache[args]
    return warpper
    
@memoize 
def recursive_fibo(n):
    return n if n < 2 else recursive_fibo(n-1) + recursive_fibo(n-2)
```
	실행 결과	
	recursive_fibo(5)

	{(2,): 1, (0,): 0, (1,): 1}
	{(2,): 1, (0,): 0, (3,): 2, (1,): 1}
	{(2,): 1, (0,): 0, (3,): 2, (1,): 1, (4,): 3}

#### REFACTORING
```python
def memoize(func):
    _cache = {}
    def warpper(*args):
        if args in _cache:
            print(_cache)
            return _cache[args]
        else:
            # dic의 upadate를 이용한 refactoring
            #_cache[args] = func(*args)    
            #return _cache[args]
            return _cache.update({args: func(*args)}) or _cache[args]
    return warpper
```

	tip) 함수형 프로그래밍
	- Function(stateless), CommonLish(Scheme), O'Caml
	- SICP("컴퓨터 프로그래밍의 구조와 해석; 이광근")

#### Class, Object == Instance
- 사람 Class
- A는 객체다 (Object) 다.
- A는 사람 Class 의 인스턴트 (Instance) 다.
