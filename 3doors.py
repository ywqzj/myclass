# -*- coding: cp936 -*-
#三门问题
from random import randint

my_change = 0
my_stay = 0
total = 100000

for n in range(total):
    my_choice = randint(0,2)
    car = randint(0,2)
    if my_choice != car:
        my_change += 1 #原来选择错了，换了就对了
    else:
        my_stay += 1  #选对了，不换就对了
        
print '换的次数是',my_change
print '换的胜率是%.2f%%'%(1.0*my_change/total)
print '不换的次数是',my_stay
print '不换的胜率是%.2f%%'%(1.0*my_stay/total)
