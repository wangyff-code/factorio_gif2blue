from trans_fun import *



def read_flam():
    size = 5
    f1 = np.zeros((size,size),dtype=int)
    list_ = []
    for i in range(size):
        for k in range(size):
            f2 = copy.copy(f1)
            f2[i][k] = 255
            list_.append(f2)
    return list_


p1 = {}
flam_list = read_flam()
print(flam_list)
gen_all(flam_list,p1)

