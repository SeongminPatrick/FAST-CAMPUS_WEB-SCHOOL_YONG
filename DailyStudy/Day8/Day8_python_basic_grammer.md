# 파이썬 기본 문법

- 인터프린터(해석기)가 내장된 script언어
- REPL => Read Eval Print Loop
- PEP ( Python Enhancement Proposal ) => PEP8 - Python Style Guide
 

#####  자료형
- Number
- String
- Boolean
######  여러 elements를 다루기 위한 자료형
- List(*) - elements, ordir O, duplicatie O
    - 참조 List[시작:끝:간격]   
    - reverse => animals[::-1]
    - 리스트안에는 모든 자료형이 들어갈 수 있다.

```python
    a = [
        [0, 1, 2],
        [3, 4, 5],
        [6, 7, 8],
    ]
```
- set(집합) - elements, order X, duplicate X
    - set([1, 1, 2, 2, 3])
    - 리스트에서 중복을 포함하지 않는 데이터만 다시 리스트로 만드는 작업
        - list => set => list
        - animals => set(animals) # 순서 보장 안됨 => list(set(animals))

- Dict(사전) - elements... O, key -> value, order X, duplicate X

```python
    student = {
        "name": "문용필",
        "email": "m71661@gmail.com",
    }
```
- Tuple - elements O, order O, duplicate O, (변하지 X)

```python
    a, b = (100, 200)
```
#####  Loop

- list for문

```python
    for animal in animals:
        print (animal)
        
    for i in range(len(animals)):
        print (animals[i])
```
- Dic for문
 
```python
    for i in student:
        print(i, "=>", student[i]) 
    
    for something in student.items(): # items()는 튜플을 반환 한다
        key, value = something
        print (key, "=>", value)
    
     for key,value in student.items():
        print (key, "=>", value)
```        

[['문용필', 'm71661@gmail.com', '010-4011-7166'],
 ['문용필2', 'm71662@gmail.com', '010-4011-7162'],
 ['문용필3', 'm71663@gmail.com', '010-4011-7163']]
 
 => 위의 데이터를 아래 형식으로 바꾸기
 
 {1: {'Name': '문용필', 'phone': '010-4011-7166', 'Email': 'm71661@gmail.com'}, 2: {'Name': '문용필2', 'phone': '010-4011-7162', 'Email': 'm71662@gmail.com'}, 3: {'Name': '문용필3', 'phone': '010-4011-7163', 'Email': 'm71663@gmail.com'}}

```python 
    dic = {}
    
    for i in range(len(students)):
        student = students[i]
        
        dic_data ={}
        
        dic_data["Name"] = student[0]
        dic_data["Email"] = student[1]
        dic_data["phone"] = student[2]
        
        dic[i+1] = dic_data
        
    print (dic)
```



        