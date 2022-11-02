
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-11-2


Contest   : Kakao_2019 winter internship # 4

Problem   : 징검다리 건너기

Algorithm : 1. Stone == 0 인 징검다리 용 돌이 연속해서 K개 존재할 경우 더 이상 건널 수 없음 ( 종료 조건 ) 

            2. 이분 탐색 

               => 이분 탐색은 탐색 범위를 절반으로 나눠서 탐색 함으로 시간 복잡도가 O(nlogm)  n : 디딤돌의 수  m : 디딤돌에 적힌 최대값

                  본래 이분탐색은 mid 값을 설정하여, 범위 내의 특정 값을 찾기 위해 사용하는 방법 

                  이러한 개념을 이 문제에 적용하면,

                    * 징검다리를 건너갈 수 있는 니니즈의 수 : mid 로 가정 , 0 ~ max(stones)  , mid = (start+end) // 2

                    * stone < mid 
                   
                      mid와 디딤돌에 적힌 숫자와의 비교를 통해, stone < mid 일 경우, 디딤돌에 적힌 life가 0을 의미하며 , 이 경우 jump_cnt ++

                      '연속적'으로 stone < mid 조건이 성립하여, jump_cnt == k 일 경우 

                      디딤돌's life가 0인 디딤돌이 k개 존재하는 것(건너지 못하는 조건)을 의미 


            3. jump_cnt == k 인 이유 ( jump_cnt > k 가 아닌 이유 ) 

               =>  jump_cnt = 0 일떄, 1칸씩 이동

                   jump_cnt = 1 일떄, 2칸씩 이동 

                   ...

                   jump_cnt = k 일떄, k+1칸씩 이동을 의미 , 최대 이동 가능한 칸은 k칸임으로 종료 조건으로 적합 


'''

def jump(stones, k, mid):
    
    jump_cnt = 0 

    for stone in stones :

        # jump_cnt = 1 일떄, stone life point 가 mid보다 작으면 1칸씩 이동하는 방법으론 더이상 이동 불가능 따라서 jump_cnt 증가
        if stone < mid :

            jump_cnt += 1

        # stone life point가 mid보다 크면, 현재 가정한 니니즈의 수(mid) 보다 더 건널 수 있음
        else : 
            jump_cnt = 0

        #  >= : Algorithm 3 참조 
        if jump_cnt == k :
            return False

    return True




def solution(stones, k):

    start, end = 0 , max(stones)

    # k == 1 이면, 각 stone life의 최소값이 정답
    if k == 1 : return min(stones)

    # start == end 이면, start가 정답 
    while start < end-1 :

        mid = (start + end) // 2

        # 건너간 니니즈의 수가 감당 가능하다면, mid 보다 큰 범위를 조사 -> start 조정
        if jump(stones, k, mid) :

            start = mid

        # 감당 가능하지 않다면, mid보다 작은 범위 조사 -> end 조정 
        else:

            end = mid 

    print(start)




solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
