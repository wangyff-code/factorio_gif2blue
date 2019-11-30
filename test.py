from trans_fun import *



def read_flam():
    f1 = np.ones((3,3),dtype=int)
    f1 = f1*255
    list_ = []
    for i in range(0,20):
        list_.append(f1)
    return list_


p1 = {}
flam_list = read_flam()
gen_all(flam_list,p1)

