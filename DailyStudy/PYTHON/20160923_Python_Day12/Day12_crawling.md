# Naver Blog crawling


#### 접속이 막혔을 때
1. IP :: Server IP(AWS EC2), IP를 변경
2. 초당 Request ... 기다림 or IP변경
3. HTTP Request Headers(Meta)로 인해 막혔을 때
	- Python, Ruby, Node.js => 'python::requests', 'ruby::__', 'node:reqiest'
	- HTTP Header에는 각 언어에서 crawling에 사용되는 라이브러리 정보가 있다.
	- 서버에서 craling에 사용되는 라이브러리를 막아 놓았을 경우 다른 기기에서 접속한 것 처럼 Http Header의 User agent정보를 바꾸어 준다.
	
```python
import requests
from bs4 import BeautifulSoup

IPAD_USER_AGENT = "Mozilla/5.0 (iPad; U; CPU OS 3_2_1 like Mac OS X; en-us) AppleWebKit/531.21.10 (KHTML, like Gecko) Version/4.0.4 Mobile/7B405 Safari/531.21.10" #i pad user agent

response = requests.get(
    "https://search.naver.com/search.naver?where=post&sm=tab_jum&ie=utf8&query=%EC%BB%A4%ED%94%BC",
    headers={
        "User-Agent": IPAD_USER_AGENT,
    }
)

result = BeautifulSoup(response.text, "html.parser")
elements = result.select("ul#addParemt li.api_bx") # user agent를 ipad로 바꾸어 주었기 때문에 CSS selector도 ipad용으로 바꾸어 주어야 한다.

for element in elements:
    print(element.select_one("div.total_tit").text)
```
	- 수행결과
	Bolivia SHB (볼리비아 커피)
	로스팅로보_언더토우, 밀크커피(라떼)
	연남동카페 커피식탁
	특별한 커피, 손쉬운 핸드드립! 스타벅스 케멕스 추출방법을 아시나요?
	샌프란시스코에서 다녀온 블루보틀 커피(Blue Bottle Coffee)
	스타벅스 커피나무, 어디까지 알고 계신가요?
	커피나무와 다육이 분갈이
	[하와이] 더 커피 쉑 The Coffee Shack : 빅아일랜드 코나 맛집
	오늘, 커피, 가을
	마포 카페 ★ 프릳츠 커피 컴퍼니 넘나 정겨운곳!
	아프리카 검은 대륙의 진주 <잠비아 커피>
	강남역카페 수수커피
	성북동카페 카페일상 드립커피의 명인이 만들어주는 가을을 닮은 커피
	도쿄여행 나카메구로 오니버스커피
	서울 용산구 한남동 '탐스커피 팝업스토어' FUSS

# Daum Blog crawling

```python
# 1 ~ 10 페이지까지의 결과를 
# CSV 파일로 저장한다.
# 함수 ( input: 키워드, 페이지수 ) => 입력받은 키워드, 입력받은 페이지수 
# 딕셔너리의 리스트
# [{"title": "___________________________", "url": __________________, "blog_title": "________________________"}, ] return 


response = requests.get("http://search.daum.net/search?w=blog&nil_search=btn&DA=NTB&enc=utf8&q=%ED%8C%8C%EC%9D%B4%EC%8D%AC")

bs = BeautifulSoup(response.text, "html.parser")
post_elements = bs.select("ul#blogResultUl li")

titles = post_element.select_one("div.wrap_tit a").text::

# ul#blogResultUl li ... 
# ul#blogResultUl > li ...  : 바로 아래 li를 가지고 온다. 
```

# Zigbang crawling
