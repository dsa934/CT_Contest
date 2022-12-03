
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-12-03


Contest   :  Basic level 0  ( level 0 의 경우, 참신한 아이디어 위주로 기록 )

Algorithm :  사격형의 넓이 구하기 max, min만 사용 

             * zip, 직접구하기 등 여러 방법이 있지만, 가장 깔끔하게 접근할 수 있는 max, min 접근법 사용 


< 알아 두기 >

 1. max_min 접근법

   => 사각형의 넓이를 구하기 위해서는 기울기를 이용 
  
      * 우상단(1시 방향),  좌하단(7시 방향)

      * 위 두 좌표를 비교하면 x 변화량 , y변화량 계산 가능

      * 우상단 좌표 max(dots) 

      * 좌하단 좌표 min(dots)

      * 음수가 포함되는 경우 꼭 우상단, 좌하단으로 구분되진 않지만, 서로 대각선에 있는 좌표로 구별 됨 

      * 기울기 : delta_y / delta_x  , 넓이 : delta_y * delta_x 
 

'''

def solution(dots):

    print(max(dots), min(dots))

    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])


solution([[1, 1], [2, 1], [2, 2], [4, -1]])