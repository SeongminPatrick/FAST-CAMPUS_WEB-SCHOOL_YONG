####block
- size가 변경되어도 공간은 전체를 차지하여 옆에 다른요소가 올 수 없다.
- block요소는 전체를 차지해서 size를 정하지 않으면 margin: 0 auto 가 적용되지 않는다.

####inline-block
- block에서 inline으로 변한 것
- inline과 다르게 size변경 가능하고 block과 다르게 옆에 다른 요소가 올 수 잇다. 
####inline
- size변경 안됨
- margin은 좌우만 유효하고 상하는 적용이 안된다..

- base-aline: 앞 요소에 마진이 있으면 앞요소에 맞춘다(default)
- vertical-aline : 블록요소 안쪽에 있는 inline요소들에게 주어서 vertical을 조정

####relative
- 자신의 위치를 바꾸기 위해서는 (ex: left:50%) position:relative를 설정해 주어야 한다.

####absolute
- 상위 부모중에서 static속성이 아닌 것을 기준으로 동작
- block에서 absolute를 주면 블럭요소의 특성을 잃어 버린다.
- 상위 부모가 position이 없으면 body를 기준으로 한다.
- absolute를 적용하면 다음요소 들에게 영향을 주지 않는다.	
