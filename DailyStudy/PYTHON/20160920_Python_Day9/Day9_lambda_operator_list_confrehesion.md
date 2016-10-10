# 파이썬 연습

- 3의  배수에 fast를 출력하는 함수
```python
fast = []
def fast(n):
    for i in range(100):
		fast.append("fast") if (i+1) % 3 == 0 else fast.append("")
```

- 3의 배수 fast, 5의 배수 campus, 15의 배수 fastcampus 출력
```python
result = []
n = 100
for i in range(n):
    element = ("fast" if i%3 == 0 else "") + ("campus" if i%5 == 0 else "")
    result.append(element)
```

- MAP 
	- list에 동일한 function 적용
	- 함수의 매개변수는 항상 1개, 출력은 list
```python
list(map(lambda x: "fast" if (x+1) % 3 == 0 else "",range(100)))
```
- FILTER
	- 참인 값만 반환하여 리스트로 출력
	- 함수의 매개변수는 항상 1개, 출력은 list
	
- REDUCE
	- REDUCE를 이용해서 rent, deposit 합 구하기 
```python
data = [
    {"rent": 50, "deposit": 1000},
    {"rent": 55, "deposit": 2000},
    {"rent": 60, "deposit": 6000},
]
```
```python
reduce(lambda x, y: x["rent"] + y["rent"], data) #잘못된 접근(처음 계산 후 결과값은 정수가 되어 150["rent"]를 호출 하게되고 오류가 발생한다.
```


```python
reduce(
    lambda x,y: {"rent": x["rent"] + y["rent"], "deposit": x["deposit"] + y["deposit"]},data #데이터 형식을 유지하면서 더해 주어야 한다.
)
```
- List Confrehension -  내부적으로 lambda와 map으로 구현되 있음
```python
["fast" if (x+1) % 3 == 0 else "" for x in range(100)]
```

		tip) 하둡의 MapReduce방식도 이와같은 map과 reduce로 인해 구현 되있습니다. 대용량 데이터에 map을 이용하여 전처리하고 reduce를 이용하여 결과 값을 뽑아 냅니다 

#### range(1, 10 +1) 제곱 중에서, 50보다 큰 수 만 리스트만들기

- for

```python
result = []
for num in range(1, 10 + 1):
    double = num * num
    if double > 50:
        result.append(double)
print (result)
```

- lamda
```python
list(filter(lambda x: x > 50,map(lambda x: x*x ,range(1, 10 + 1))))
```
- list comprehension
	- list comprehension은 map과 filter를 한번에 할 수 있게 해 준다.
```python
[
    x*x
    for x 
    in range(1, 10 + 1) 
    if x*x > 50
]
``` 
	tip) pep8 자동 체크 툴: pep8

#### arg, kwargs
```python
def hello(*args):     # 함수를 정의하는 시점 :: pack! 여러 요소가 들어오면 하나의 튜플로 묶어서 받는다.

hello(*data)             # 함수를 호출하는 시점 :: unpack! 리스트 처럼 묶여 있는 요소들을 풀어서 따로 따로 전달한다.
    print(args)
```