# -*- coding: cp936 -*-
#��������
from random import randint

my_change = 0
my_stay = 0
total = 100000

for n in range(total):
    my_choice = randint(0,2)
    car = randint(0,2)
    if my_choice != car:
        my_change += 1 #ԭ��ѡ����ˣ����˾Ͷ���
    else:
        my_stay += 1  #ѡ���ˣ������Ͷ���
        
print '���Ĵ�����',my_change
print '����ʤ����%.2f%%'%(1.0*my_change/total)
print '�����Ĵ�����',my_stay
print '������ʤ����%.2f%%'%(1.0*my_stay/total)
