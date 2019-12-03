from trans_fun import *



def read_flam():
    size = 32
    f1 = np.zeros((size,size),dtype=int)
    for i in range(size):
        for k in range(size):
            f1[i][k] = 255
    list_ = []
    for i in range(5):
        list_.append(f1)
    return list_


p1 = {}
flam_list = read_flam()
print(flam_list)
gen_all([flam_list],p1)

# print(unsigned_signed(3000000000))
