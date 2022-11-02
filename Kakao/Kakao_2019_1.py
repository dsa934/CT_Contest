
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-11-02


Contest   : Kakao_2019 winter internship # 1

Problem   : 크레인 인형뽑기 게임 

Algorithm : 문제에서 요구하는데로 풀이 , Stack 사용 


< 알아 두기 >


< 반성 point >

 1. 사라진 인형의 수를 계산 해야 하는데,  사라진 횟수를 계산해서 쓸데없는 시간 소모


'''

def solution(board, moves):
    
    basket, score = [], 0 

    len_row = len(board)
    
    for val in moves:

        pos_col = val - 1 

        for pos_row in range(len_row):

            if board[pos_row][pos_col] != 0 :

                basket.append(board[pos_row][pos_col])

                board[pos_row][pos_col] = 0

                break

        if len(basket) > 1 : 

            if basket[-1] == basket[-2] : 
                
                score +=2

                basket.pop()
                basket.pop()


    print(score)


solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]] , [1,5,3,5,1,2,1,4] )