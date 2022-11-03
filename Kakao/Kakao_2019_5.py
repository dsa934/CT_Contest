
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-11-2


Contest : Kakao_2019 winter internship # 5

Problem : ȣ�� �� ���� 


< �˾� �α� >

 1. dict �ڷ����� get 
  
   =>  room = {} 

       value = room.get(0, 0)

       * room dict �� key ������ 0�� ���� ��� value ������ 0�� �Ҵ� 


 2.  ��� üũ / ��ü ���ȣ ���� / ���ݱ��� ���Ŀ� ����� ��ü ���ȣ �ֽ�ȭ 
 
     * ���� �ִ� ��� : �� ���� 
 
     * ���� ���� ��� 

        - �� ���� ã�� ���� ���İ��� ���� ������ tmp_drop_by ����

        _ ��ü ���ȣ�� �������� ���� �ִ��� ������ üũ

          a) ���� ���� ��� : ���信 ���ȣ �߰�, ������ ���� ��ü ���ȣ ����, �������� ���Ŀ� �� ��ȣ�� ��ü ���ȣ�� �ֽ�ȭ 

          b) ���� ���� ��� : tmp_drop_by �� �� ��ȣ�� �߰� 

    


< �ݼ� point >


 1. ù �õ��� TLE

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


    *  room_number ũ�� <= 200,000 ������ not in �� ���� ���Ҷ����� 20�� ���� ���ؾ� �� 

    * indexing �� ������ �湮 ����Ʈ �ۼ� �� ��� ���� �̶�� ���̵� ��� �ؾ� ���� 


       
'''








def solution(k, room_numbers):

    answer = [] 

    # �θ� ��� ���� ���踦 ���� dict
    visited = {} 

    for n_room in room_numbers:

        reserved = visited.get(n_room, 0)

        # ���� ������
        if reserved == 0 :

            answer.append(n_room)

            # ������ ���� �θ� ��� ���� 
            visited[n_room] = n_room + 1 


        # ���� ������ 
        else:

            # �� ���� ã�� ���� ���İ� �� ������ ���� list
            tmp_drop_by = [n_room]

            while True :

                # ������ ���� ��������� ���, ��ü���� ���õ� �� ��ȣ 
                order_room = reserved

                # ��ü ���ȣ�� ����ִ��� Ȯ�� 
                reserved = visited.get(order_room, 0)
                
                # ���� ������ 
                if reserved == 0 :

                    answer.append(order_room)

                    # ������ ���� �θ� ��� ���� 
                    visited[order_room] = order_room + 1

                    # ���� ���� ���� �� ����� ��ü����� ��� ����� ���� ������ ���� ���·� �� �� ���� 
                    # ���� tmp_drop_by list�� ����ִ� ��� ���� ���� ��ü�� ��ȣ  �ֽ�ȭ 
                    for drop in tmp_drop_by :

                        visited[drop] = order_room + 1 

                    break


                # ���� ������ 
                else:
                    tmp_drop_by.append(reserved)

                

    print(answer)
    


solution(10, [1,3,4,1,3,1])