
# -*- coding: cp949 -*-

'''

 Author / date : Jinwoo Lee / 2022-12-04


Contest   :  Basic level 0  ( level 0 �� ���, ������ ���̵�� ���ַ� ��� )

Algorithm :  ���ڿ� �б� 


< �˾� �α� >

 1. ���ڿ� ���� ��� 

    * ��� ���ڿ�(B)�� 2�� ���Ѵ�  

       => if B = 'ABCD ' then B*2 = 'ABCDABCD'

    * ã�ƾ� �ϴ� �� ���ڿ�(A)�� ���� ��ġ�� b���� ã�´�

       => B*2.find(A)

       => a�� ������ġ = ���ڿ� �б� Ƚ�� 


    * index �Լ��� ��� ã������ ����� ������ error �߻� 

    * find ã�� ����� ���� ��� -1 return 


 
 

'''

solution = lambda a,b:(b*2).find(a)