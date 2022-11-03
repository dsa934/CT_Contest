
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-11-2


Contest : Kakao_2019 winter internship # 5

Problem : 호텔 방 배정 


< 알아 두기 >

 1. dict 자료형의 get 
  
   =>  room = {} 

       value = room.get(0, 0)

       * room dict 의 key 값으로 0이 없을 경우 value 변수에 0을 할당 


 2.  빈방 체크 / 대체 방번호 설정 / 지금까지 거쳐온 방들의 대체 방번호 최신화 
 
     * 방이 있는 경우 : 방 배정 
 
     * 방이 없는 경우 

        - 빈 방을 찾기 위해 거쳐가는 방을 저장할 tmp_drop_by 설정

        _ 대체 방번호를 기준으로 방이 있는지 없는지 체크

          a) 방이 있을 경우 : 정답에 방번호 추가, 배정된 방의 대체 방번호 설정, 이전까지 거쳐온 방 번호의 대체 방번호를 최신화 

          b) 방이 없는 경우 : tmp_drop_by 에 방 번호만 추가 

    


< 반성 point >


 1. 첫 시도에 TLE

     def find_value(value, answer):
    

        while True :

            value += 1

            if value not in answer : 

               return value


    def solution(k, room_number):


        answer = [] 

        for value in room_number:

            if value not in answer :

                answer.append(value)

            else:

                answer.append( find_value(value, answer) )


        print(answer)


    *  room_number 크기 <= 200,000 임으로 not in 을 통해 비교할때마다 20만 개를 비교해야 함 

    * indexing 이 가능한 방문 리스트 작성 및 노드 연결 이라는 아이디어를 사용 해야 했음 


       
'''








def solution(k, room_numbers):

    answer = [] 

    # 부모 노드 연결 관계를 위한 dict
    visited = {} 

    for n_room in room_numbers:

        reserved = visited.get(n_room, 0)

        # 방이 있으면
        if reserved == 0 :

            answer.append(n_room)

            # 배정한 방의 부모 노드 설정 
            visited[n_room] = n_room + 1 


        # 방이 없으면 
        else:

            # 빈 방을 찾기 위해 거쳐간 방 저장을 위한 list
            tmp_drop_by = [n_room]

            while True :

                # 선택한 방이 예약되있을 경우, 대체제로 선택된 방 번호 
                order_room = reserved

                # 대체 방번호가 비어있는지 확인 
                reserved = visited.get(order_room, 0)
                
                # 방이 있으면 
                if reserved == 0 :

                    answer.append(order_room)

                    # 배정된 방의 부모 노드 설정 
                    visited[order_room] = order_room + 1

                    # 지금 까지 거쳐 온 방들의 대체방들이 모두 예약된 상태 임으로 연결 상태로 볼 수 있음 
                    # 따라서 tmp_drop_by list에 들어있는 모든 방의 대한 대체방 번호  최신화 
                    for drop in tmp_drop_by :

                        visited[drop] = order_room + 1 

                    break


                # 방이 없으면 
                else:
                    tmp_drop_by.append(reserved)

                

    print(answer)
    


solution(10, [1,3,4,1,3,1])