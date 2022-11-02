
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-11-2


Contest   : Kakao_2019 winter internship # 3

Problem   : �ҷ� �����

Algorithm : 1. ���� ������ ���� ���� �࿡ ���ϱ� ������ ���� �������� ���� Ǯ�� ���� 

            2. user_list �� Permutations ���� �����ϱ� ( �ݼ��ϱ� 1-2 )



< �˾� �α� >

 1. Zip 

   => ������, 2�� �̻��� list�� ���Ͽ� �� ����Ʈ�� ���Ҹ� ���� ���� ��� zip�� Ȱ���ϱ� 



< �ݼ� point >

 1. �ߺ� ó���� ���� ��� 
 
   ���� �õ�, �� banned_id type �� ���ϴ� �ܾ dict[banned_type] = [user1, user2, ..] �� �������·� ����������,

   banned_id type�� �ߺ��� ���, ������ �ذ��ϴ� ������ �������� 

   => ������ ���� ��, ������ ũ�⸦ ���� ���� ���� ũ���� ������������ �����غ��� 

                      ������ ũ�Ⱑ ����� ũ�ٸ� ����п� ���ؼ� �ٽ� ����


 2. Permutation ( not Combinations )

   => [ "fr*d*", "*rodo", ... ]  �� ���� ban type ������ �� 

       user_list 1 : [frodo , fradi, abc123, frodoc]

       user_list 2 : [fradi,  frodo, abc123, frodoc]

       ���� ��Ҵ� ���� ������, ban ���ǰ� ���ϴ� ������ ���� ������ �ɼ���, �ƴҼ��� �ֱ� ������
       
       �̸� ������ ó���ϱ� ���ٴ� , user_list�� �ߺ��� �����Ͽ� �����ϰ�, 
       
       ���� ���� list�� �߰��Ҷ���  ���� list�� ���ԵǾ��ִ��� Ȯ���ϰ�, set�� ���·� �߰�


'''


from itertools import permutations


def solution(user_id, banned_id):

    answer = []

    num_ban = len(banned_id)

    user_set = list(permutations(user_id, num_ban))


    for user_list in user_set:

        user_flag = True

        # zip �� Ȱ���Ͽ� ban1 user1 �� 
        for user, ban in zip(user_list, banned_id):

            # ���̰� �ٸ� ��� false
            if len(user) != len(ban) : 

                user_flag = False
                break

            # �ܾ� �ϳ��ϳ� ��
            for char_user, char_ban in zip(user, ban):

                if char_user != char_ban :

                    if char_ban != '*':

                        user_flag = False
                        break

        if user_flag :

            if set(user_list) not in answer:

                answer.append(set(user_list))

    print(len(answer))



solution(["frodo", "fradi", "crodo", "abc123", "frodoc"] , ["fr*d*", "*rodo", "******", "******"] )