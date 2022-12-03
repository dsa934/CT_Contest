
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-12-03


Contest   :  Basic level 0  ( level 0 �� ���, ������ ���̵�� ���ַ� ��� )

Algorithm :  ������� ���� ���ϱ� max, min�� ��� 

             * zip, �������ϱ� �� ���� ����� ������, ���� ����ϰ� ������ �� �ִ� max, min ���ٹ� ��� 


< �˾� �α� >

 1. max_min ���ٹ�

   => �簢���� ���̸� ���ϱ� ���ؼ��� ���⸦ �̿� 
  
      * ����(1�� ����),  ���ϴ�(7�� ����)

      * �� �� ��ǥ�� ���ϸ� x ��ȭ�� , y��ȭ�� ��� ����

      * ���� ��ǥ max(dots) 

      * ���ϴ� ��ǥ min(dots)

      * ������ ���ԵǴ� ��� �� ����, ���ϴ����� ���е��� ������, ���� �밢���� �ִ� ��ǥ�� ���� �� 

      * ���� : delta_y / delta_x  , ���� : delta_y * delta_x 
 

'''

def solution(dots):

    print(max(dots), min(dots))

    return (max(dots)[0] - min(dots)[0]) * (max(dots)[1] - min(dots)[1])


solution([[1, 1], [2, 1], [2, 2], [4, -1]])