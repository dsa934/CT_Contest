
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-11-2


Contest   : Kakao_2019 winter internship # 2

Problem   : Ʃ��

Algorithm : 1. ���ڿ��� �Է��� �ޱ� ������ . replace, split�� ���� ���ڿ��� ���� �ִ� �� �κ������� ��ҵ��� listȭ 

            2. �� �κ������� ���� ������ �������� ���� �����ν� ���� Ʃ�ÿ� ���� ������ ���� 


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

        #  2�ڸ� �� �̻��� ���ڰ� ���ԵǴ� ��츦 handling �ϱ� ���� ��� 
        num_list = sub_str.split(',')
        
        save_dict[len(num_list)] = num_list
        

    sorted_dict = sorted(save_dict.items() )

    for num_list in sorted_dict:

        for value in num_list[1]:

            if int(value) not in answer :

                answer.append(int(value))

    print(answer)

solution("{{20,111},{111}}")