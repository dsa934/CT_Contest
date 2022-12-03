
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-12-04


Contest   :  Basic level 0  ( level 0 의 경우, 참신한 아이디어 위주로 기록 )

Algorithm :  문자열 밀기 


< 알아 두기 >

 1. 문자열 곱셈 사용 

    * 대상 문자열(B)를 2번 곱한다  

       => if B = 'ABCD ' then B*2 = 'ABCDABCD'

    * 찾아야 하는 비교 문자열(A)의 시작 위치를 b에서 찾는다

       => B*2.find(A)

       => a의 시작위치 = 문자열 밀기 횟수 


    * index 함수의 경우 찾으려는 대상이 없으면 error 발생 

    * find 찾는 대상이 없는 경우 -1 return 


 
 

'''

solution = lambda a,b:(b*2).find(a)