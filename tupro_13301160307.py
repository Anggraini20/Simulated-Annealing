from random import uniform
import math
def sa(x1,x2) :
    return -abs(math.sin(x1) * math.cos(x2) * math.exp(abs(1 - math.sqrt(x1 * x1 + x2 * x2) / 3.14)))

cur_state1 = uniform(-10,10) #cari bil random untuk current state
cur_state2 = uniform(-10,10) #cari bil random untuk current state
T_MAX = 1
BSF1 = cur_state1
BSF2 = cur_state2
T_MIN = 0.0001
T_CUR = T_MAX #suhu sekarang di assign dengan suhu maksimal
while T_CUR> T_MIN :
    new_state1 = uniform(-10, 10)
    new_state2 = uniform(-10, 10)
    if sa(cur_state1,cur_state2)> sa(new_state1,new_state2) :
        cur_state1 = new_state1
        cur_state2 = new_state2
        if sa(BSF1,BSF2)> sa(cur_state1,cur_state2) :
            BSF1 = cur_state1
            BSF2 = cur_state2
    else:
        if math.exp(- (sa(new_state1,new_state2) - sa(cur_state1,cur_state2))/T_CUR) < 0.4 : #mengecheck probabilitas
            cur_state1 = new_state1
            cur_state2 = new_state2
    T_CUR = T_CUR *0.9999 #mengurahi suhu
    print('x1: ', BSF1)
    print('x2 : ',BSF2)
    print(sa(BSF1,BSF2))