
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-11-2


Contest   : Kakao_2019 winter internship # 3

Problem   : 불량 사용자

Algorithm : 1. 제한 조건이 비교적 작은 축에 속하기 떄문에 완전 구현으로 문제 풀이 진행 

            2. user_list 를 Permutations 으로 구성하기 ( 반성하기 1-2 )



< 알아 두기 >

 1. Zip 

   => 앞으로, 2개 이상의 list에 대하여 각 리스트의 원소를 서로 비교할 경우 zip을 활용하기 



< 반성 point >

 1. 중복 처리에 대한 고민 
 
   최초 시도, 각 banned_id type 에 속하는 단어를 dict[banned_type] = [user1, user2, ..] 의 사전형태로 구성했으나,

   banned_id type이 중복일 경우, 문제를 해결하는 과정이 복잡해짐 

   => 문제를 읽을 떄, 조건의 크기를 보고 비교적 작은 크기라면 완전구현으로 생각해보기 

                      조건의 크기가 충분히 크다면 방법론에 대해서 다시 생각


 2. Permutation ( not Combinations )

   => [ "fr*d*", "*rodo", ... ]  과 같은 ban type 형태일 때 

       user_list 1 : [frodo , fradi, abc123, frodoc]

       user_list 2 : [fradi,  frodo, abc123, frodoc]

       구성 요소는 동일 하지만, ban 조건과 비교하는 순서에 따라 정답이 될수도, 아닐수도 있기 떄문에
       
       이를 일일히 처리하기 보다는 , user_list를 중복을 포함하여 구축하고, 
       
       최종 정답 list에 추가할때는  정답 list에 포함되어있는지 확인하고, set의 형태로 추가


'''


from itertools import permutations


def solution(user_id, banned_id):

    answer = []

    num_ban = len(banned_id)

    user_set = list(permutations(user_id, num_ban))


    for user_list in user_set:

        user_flag = True

        # zip 을 활용하여 ban1 user1 비교 
        for user, ban in zip(user_list, banned_id):

            # 길이가 다를 경우 false
            if len(user) != len(ban) : 

                user_flag = False
                break

            # 단어 하나하나 비교
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