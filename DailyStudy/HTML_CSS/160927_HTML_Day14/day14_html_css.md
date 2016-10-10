#Day13_HTML/CSS

####emmet 사용법

####display

- Inline
	- inline 좌우 margin을 제외하고는 어떤 길이 속성도 영향을 받지 않는다.
- None
	- visaulbility: hidden과 다르게 공간도 차지하지 않는다.
- Block
	- 가운데 정렬 : margin: 0 auto
- InlineBlock
	- inline요소와 다르게 상하 높이를 줄수 있다.
	
####float

- float속성이 들어오면 block요소의 특성을 잃어 버린다.
- float속성이 적용되면 다른 block요소의 침범을 받는다.

####clear
- float요소와 겹치는 경우 float속성을 무시합니다.
- 부모요소가 float속성을 가진 자식요소를 인식하는 방법 3가지 :
	- <br style
	
#### position
- relative : 자기 시작위치로 부터 이동
- fixed: 무조건 한곳에 고정
- absolute : 부모를 기준으로 이동, absolute의 부모가 static이면 안된다.

#### block 요소 정렬
- div요소 가로 가운데 정렬 => margin: 0 auto
- div 요소 세로 가운데 정렬 => position: relative, top:50%,   transform: translateY(-50%);



