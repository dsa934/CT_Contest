
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-11-2


Contest   : Kakao_2019 winter internship # 4

Problem   : ¡�˴ٸ� �ǳʱ�

Algorithm : 1. Stone == 0 �� ¡�˴ٸ� �� ���� �����ؼ� K�� ������ ��� �� �̻� �ǳ� �� ���� ( ���� ���� ) 

            2. �̺� Ž�� 

               => �̺� Ž���� Ž�� ������ �������� ������ Ž�� ������ �ð� ���⵵�� O(nlogm)  n : ������� ��  m : ������� ���� �ִ밪

                  ���� �̺�Ž���� mid ���� �����Ͽ�, ���� ���� Ư�� ���� ã�� ���� ����ϴ� ��� 

                  �̷��� ������ �� ������ �����ϸ�,

                    * ¡�˴ٸ��� �ǳʰ� �� �ִ� �ϴ����� �� : mid �� ���� , 0 ~ max(stones)  , mid = (start+end) // 2

                    * stone < mid 
                   
                      mid�� ������� ���� ���ڿ��� �񱳸� ����, stone < mid �� ���, ������� ���� life�� 0�� �ǹ��ϸ� , �� ��� jump_cnt ++

                      '������'���� stone < mid ������ �����Ͽ�, jump_cnt == k �� ��� 

                      �����'s life�� 0�� ������� k�� �����ϴ� ��(�ǳ��� ���ϴ� ����)�� �ǹ� 


            3. jump_cnt == k �� ���� ( jump_cnt > k �� �ƴ� ���� ) 

               =>  jump_cnt = 0 �ϋ�, 1ĭ�� �̵�

                   jump_cnt = 1 �ϋ�, 2ĭ�� �̵� 

                   ...

                   jump_cnt = k �ϋ�, k+1ĭ�� �̵��� �ǹ� , �ִ� �̵� ������ ĭ�� kĭ������ ���� �������� ���� 


'''

def jump(stones, k, mid):
    
    jump_cnt = 0 

    for stone in stones :

        # jump_cnt = 1 �ϋ�, stone life point �� mid���� ������ 1ĭ�� �̵��ϴ� ������� ���̻� �̵� �Ұ��� ���� jump_cnt ����
        if stone < mid :

            jump_cnt += 1

        # stone life point�� mid���� ũ��, ���� ������ �ϴ����� ��(mid) ���� �� �ǳ� �� ����
        else : 
            jump_cnt = 0

        #  >= : Algorithm 3 ���� 
        if jump_cnt == k :
            return False

    return True




def solution(stones, k):

    start, end = 0 , max(stones)

    # k == 1 �̸�, �� stone life�� �ּҰ��� ����
    if k == 1 : return min(stones)

    # start == end �̸�, start�� ���� 
    while start < end-1 :

        mid = (start + end) // 2

        # �ǳʰ� �ϴ����� ���� ���� �����ϴٸ�, mid ���� ū ������ ���� -> start ����
        if jump(stones, k, mid) :

            start = mid

        # ���� �������� �ʴٸ�, mid���� ���� ���� ���� -> end ���� 
        else:

            end = mid 

    print(start)




solution([2, 4, 5, 3, 2, 1, 4, 2, 5, 1], 3)
