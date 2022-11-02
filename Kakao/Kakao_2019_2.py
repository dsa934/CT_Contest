
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-11-2


Contest   : Kakao_2019 winter internship # 2

Problem   : 튜플

Algorithm : 1. 문자열로 입력을 받기 때문에 . replace, split을 통해 문자열에 속해 있는 각 부분집합의 요소들을 list화 

            2. 각 부분집합의 길이 순으로 내림차순 정렬 함으로써 원본 튜플에 대한 추측이 가능 


'''

def solution(s):
   
    answer = [] 

    # remove { 
    s = s.replace('{', '')

    # remove }}
    s = s.replace('}}', '')

    s = s.split('},')
    
    save_dict = {}

    for sub_str in s:

        #  2자리 수 이상의 숫자가 포함되는 경우를 handling 하기 위해 사용 
        num_list = sub_str.split(',')
        
        save_dict[len(num_list)] = num_list
        

    sorted_dict = sorted(save_dict.items() )

    for num_list in sorted_dict:

        for value in num_list[1]:

            if int(value) not in answer :

                answer.append(int(value))

    print(answer)

solution("{{20,111},{111}}")