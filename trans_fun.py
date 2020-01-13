import numpy as np
import copy
from dir_fac import *
import base64
import zlib
import json
import struct


def unsigned_signed(num):
    bys = struct.pack('I',num)
    out = struct.unpack('i',bys)
    return out[0]




def gen_connect_web(cnt):
    t_dir = {}
    try:
        t_dir['entity_id']  = int(cnt[0])
        t_dir['circuit_id'] = int(cnt[1])
    except:
        t_dir['entity_id'] = int(cnt)
    return copy.deepcopy(t_dir)


def gen_sigConnect(net):
    t_dir = {}
    for i in net:
        t_dir['entity_id'] = int(i)
    




def gen_connect(p1_gen,p1_red,p2_gen,p2_red):
    t1_dir = {}
    t2_dir = {}
    t_dir = {}
    if len(p2_gen) == 0 and len(p2_red) == 0:
        connect_list = []
        if len(p1_gen) !=0:
            for i in p1_gen:
                connect_list.append(gen_connect_web(i))
            t1_dir['green'] = connect_list  
            
        connect_list = []
        if len(p1_red) !=0:
            for i in p1_red:
                connect_list.append(gen_connect_web(i))
            t1_dir['red'] = connect_list 
        t_dir['1'] = t1_dir
        return t_dir
    else:
        connect_list = []
        if len(p1_gen) !=0:
            for i in p1_gen:
                connect_list.append(gen_connect_web(i))
            t1_dir['green'] = connect_list    
        
        connect_list = []
        if len(p1_red) !=0:
            for i in p1_red:
                connect_list.append(gen_connect_web(i))
            t1_dir['red'] = connect_list 
        
        connect_list = []
        if len(p2_gen) !=0:
            for i in p2_gen:
                connect_list.append(gen_connect_web(i))
            t2_dir['green'] = connect_list 

        connect_list = []
        if len(p2_red) !=0:
            for i in p2_red:
                connect_list.append(gen_connect_web(i))
            t2_dir['red'] = connect_list 

    t_dir['1'] = t1_dir
    t_dir['2'] = t2_dir
    return t_dir


def gen_cmp(id_,x,y,costant,p1_gen,p1_red,p2_gen,p2_red):
    cmp_dir['entity_number'] = int(id_)
    cmp_dir['position']['x'] = float(x)
    cmp_dir['position']['y'] = float(y)
    cmp_dir['control_behavior']['decider_conditions']['constant'] = int(costant)
    t_dir=gen_connect(p1_gen,p1_red,p2_gen,p2_red)
    cmp_dir['connections'] = t_dir
    return copy.deepcopy(cmp_dir)


def gen_cl(id_,x,y,costant,opt,p1_gen,p1_red,p2_gen,p2_red):
    cal_dir['entity_number'] = int(id_)
    cal_dir["position"]['x'] = float(x)
    cal_dir["position"]['y'] = float(y)
    cal_dir['control_behavior']['arithmetic_conditions']["second_constant"] = costant
    cal_dir['control_behavior']['arithmetic_conditions']["operation"] = opt
    t_dir=gen_connect(p1_gen,p1_red,p2_gen,p2_red)
    cal_dir['connections'] = t_dir
    return copy.deepcopy(cal_dir)



def gen_cl_s(id_,x,y,costant,opt,p1_gen,p1_red,p2_gen,p2_red):
    temp = copy.deepcopy(cal_dir)
    temp['entity_number'] = int(id_)
    temp["position"]['x'] = float(x)
    temp["position"]['y'] = float(y)
    temp['control_behavior']['arithmetic_conditions']["second_constant"] = costant
    temp['control_behavior']['arithmetic_conditions']["operation"] = opt
    temp['control_behavior']['arithmetic_conditions']['first_signal']['name'] = 'signal-red'
    temp['control_behavior']['arithmetic_conditions']['output_signal']['name'] = 'signal-red'
    t_dir=gen_connect(p1_gen,p1_red,p2_gen,p2_red)
    temp['connections'] = t_dir
    return copy.deepcopy(temp)


class gen_class:
    def __init__(self):
        self.item_list = []
        self.id_counter = 1
        self.flam_list =[]
        self.flam_number = 0
        self.y_size = 0
        self.x_size = 0
        self.clock_mat = 0
        self.ram_mat = 0
        self.display_mat = 0
        self.slip_size = 16
    def read_flam(self,flam_in):
        self.flam_list = flam_in
        self.flam_number = len(flam_in)
        self.y_size,self.x_size=flam_in[0].shape





def gen_ram_mat(gen):
    const_number = gen.x_size//gen.slip_size + 1
    ram_mat=np.zeros((const_number+1,gen.flam_number),dtype=int)
    for x in range(0,gen.flam_number):
        for y in range(0,const_number+1):
            ram_mat[y][x] = gen.id_counter
            gen.id_counter+=1
    gen.ram_mat = ram_mat


def split_flam(gen,flam):
    temp_list = []
    data_list = []
    y_size,x_size = flam.shape
    for x in range(0,x_size):
        number = 0
        for y in range(0,y_size):
            number=number << 1
            if flam[y][x] == 255:
                number=number + 1
        number=unsigned_signed(number)
        temp_list.append([x,number])
    for i in range(0,x_size//gen.slip_size+1):
        data_list.append(copy.copy(temp_list[i*gen.slip_size:(i+1)*gen.slip_size]))
    return data_list



def place_cmp(gen,x,x_size,off_y):
    ram_mat = gen.ram_mat
    if x == 0:
        t=gen_cmp(ram_mat[0][x],-x,-1.5+off_y,p1_gen=[ram_mat[1][x]],p1_red=[[ram_mat[0][x+1],1],[gen.clock_mat[0][2],2]],p2_gen=[[ram_mat[0][x+1],2]],p2_red=[],costant= x)
    else:
        if x == x_size-1:
            t=gen_cmp(ram_mat[0][x],-x,-1.5+off_y,p1_gen=[ram_mat[1][x]],p1_red=[[ram_mat[0][x-1],1]],p2_gen=[[ram_mat[0][x-1],2]],p2_red=[],costant= x)
        else:
            t=gen_cmp(ram_mat[0][x],-x,-1.5+off_y,p1_gen=[ram_mat[1][x]],p1_red=[[ram_mat[0][x-1],1],[ram_mat[0][x+1],1]],p2_gen=[[ram_mat[0][x-1],2],[ram_mat[0][x-1],2]],p2_red=[],costant= x)
    return copy.deepcopy(t)




def gen_const(id_,x,y,p1_gen,p1_red,p2_gen,p2_red,data_list):
    con_dir ={'entity_id': 1}
    data_dir= {
                "signal": {
                    "type": "virtual",
                    "name": "signal-0"
                },
                "count": 1,
                "index": 1
            }
    cost_dir['entity_number'] = int(id_)
    cost_dir['position']['x'] = float(x)
    cost_dir['position']['y'] = float(y)
    t_dir=gen_connect(p1_gen,p1_red,p2_gen,p2_red)
    cost_dir['connections'] = copy.deepcopy(t_dir)
    connect_list = []
    for i in range(0,len(data_list)):
        data_dir["signal"]["name"] =  sig_list[data_list[i][0]][1]
        data_dir["signal"]["type"] =  sig_list[data_list[i][0]][0]
        data_dir["count"] = int(data_list[i][1])
        data_dir["index"] = int(i+1)
        connect_list.append(copy.deepcopy(data_dir))
    cost_dir['control_behavior']['filters'] = copy.deepcopy(connect_list)
    return copy.deepcopy(cost_dir)

def gen_pow(id_,x,y):
    pow_dir['entity_number'] = int(id_)
    pow_dir['position']['x'] = float(x)
    pow_dir['position']['y'] = float(y)
    return copy.deepcopy(pow_dir)

def gen_led(id_,x,y,p1_gen):
    led_dir['entity_number'] = int(id_)
    led_dir['position']['x'] = int(x)
    led_dir['position']['y'] = int(y)
    led_dir['control_behavior']['circuit_condition']['first_signal']['name'] = sig_list[x-5][1]
    led_dir['control_behavior']['circuit_condition']['first_signal']['type'] = sig_list[x-5][0]
    t_dir=gen_connect(p1_gen,[],[],[])
    led_dir['connections'] = t_dir
    return copy.deepcopy(led_dir)

def place_const(ram_mat,data_list,x,y,y_size,off_y):
    if y == y_size-1:
        t = gen_const(ram_mat[y][x],-x,y+off_y,p1_gen=[ram_mat[y-1][x]],p1_red=[],p2_gen=[],p2_red=[],data_list= data_list[y-1])
    else:
        t = gen_const(ram_mat[y][x],-x,y+off_y,p1_gen=[ram_mat[y-1][x],ram_mat[y+1][x]],p1_red=[],p2_gen=[],p2_red=[],data_list= data_list[y-1])
    return copy.deepcopy(t)



def place_pow(gen,x,y,x_st,y_st,num):
    for i in range(0,num):
        t=gen_pow(gen.id_counter,x,y)
        x += x_st
        y += y_st
        gen.id_counter += 1
        gen.item_list.append(t)


def place_ram(gen,off_y):
    y_size,x_size=gen.ram_mat.shape
    for x in range(0,x_size):
        data_list = split_flam(gen,gen.flam_list[x])
        for y in range(0,y_size):
            if y == 0:
                t=place_cmp(gen,x,x_size,off_y)
                gen.item_list.append(t)
            else: 
                    t=place_const(gen.ram_mat,data_list,x,y,y_size,off_y)
                    gen.item_list.append(t)





def pack_dir(gen):
    body_dir['blueprint']['entities'] = gen.item_list
    data = json.dumps(body_dir)
    f = open('out.json','w')
    f.write(data)
    f.close()
    data.replace(' ','')
    data.replace('\n','')
    st = data.encode('utf-8')
    st = zlib.compress(st)
    out = base64.b64encode(st).decode()
    out = '0' + out
    f = open('blue_code.txt','w')
    f.write(out)
    f.close()
    return out



def gen_clock_mat(gen):
    gen.clock_mat = np.zeros((1,3),dtype=int)
    for i  in range(0,3):
        gen.clock_mat[0][i] = gen.id_counter
        gen.id_counter += 1


def gen_display_mat(gen):
    gen.display_mat = np.zeros((gen.y_size,gen.x_size+2),dtype=int)
    y_size,x_size=gen.display_mat.shape
    for x in range(0,2):
        for y in range(0,y_size):
            gen.display_mat[y][x] = gen.id_counter
            gen.id_counter += 1


def place_clock(gen,off_y):
    
    t = gen_cl_s(gen.clock_mat[0][0],-5,-3.5+off_y,1,'+',p1_gen=[[gen.clock_mat[0][0],2]],p1_red=[],p2_gen= [[gen.clock_mat[0][0],1],[gen.clock_mat[0][1],1]],p2_red=[])
    gen.item_list.append(t)

    t = gen_cl(gen.clock_mat[0][1],-3,-3.5+off_y,10,'/',p1_gen=[[gen.clock_mat[0][0],2]],p1_red=[],p2_gen= [[gen.clock_mat[0][2],1]],p2_red=[])
    gen.item_list.append(t)

    t = gen_cl(gen.clock_mat[0][2],-1,-3.5+off_y, (gen.flam_number-1),'%',p1_gen=[[gen.clock_mat[0][1],2]],p1_red=[],p2_gen= [],p2_red=[[gen.ram_mat[0][0],1]])
    gen.item_list.append(t)




def place_select(gen,x,y,y_size,off_y):
    if y == 0:
        t = gen_cl(gen.display_mat[y][x],1.5,-y+off_y,y,'>>',p1_gen=[[gen.display_mat[y+1][x],1],[gen.ram_mat[0][x],2]],p1_red=[],p2_gen= [[gen.display_mat[y][x+1],1]],p2_red=[])
    else:
        if y == (y_size-1):
            t = gen_cl(gen.display_mat[y][x],1.5,-y+off_y,y,'>>',p1_gen=[[gen.display_mat[y-1][x],1]],p1_red=[],p2_gen= [[gen.display_mat[y][x+1],1]],p2_red=[])
        else:
            t = gen_cl(gen.display_mat[y][x],1.5,-y+off_y,y,'>>',p1_gen=[[gen.display_mat[y-1][x],1],[gen.display_mat[y-1][x],1]],p1_red=[],p2_gen= [[gen.display_mat[y][x+1],1]],p2_red=[])
    gen.item_list.append(t)

def place_and(gen,x,y,off_y):
    t = gen_cl(gen.display_mat[y][x],3.5,-y+off_y,1,'AND',p1_gen=[[gen.display_mat[y][x-1],2]],p1_red=[],p2_gen= [gen.display_mat[y][x+1]],p2_red=[])
    gen.item_list.append(t)


def place_led(gen,x,y,x_size,off_y):
    if (x-2)%7 != 0 or y%7 != 0:
        if (y%7 == 0 and x == 3) or(y%7 != 0 and  x == 2):
            t = gen_led(gen.id_counter,x+3,-y+off_y,[[gen.display_mat[y][1],2]])
        else:
            if x == (x_size-1):
                t = gen_led(gen.id_counter,x+3,-y+off_y,[gen.id_counter-1])
            else:
                t = gen_led(gen.id_counter,x+3,-y+off_y,[gen.id_counter-1,gen.id_counter+1])
        gen.id_counter+=1
        gen.item_list.append(t)    




def place_display(gen,off_y):
    y_size,x_size=gen.display_mat.shape
    for y in range(0,y_size):
        for x in range(0,x_size):
            if x == 0 :
                place_select(gen,x,y,y_size,off_y)
            else:
                if x == 1:
                    place_and(gen,x,y,off_y)
                else:
                    place_led(gen,x,y,x_size,off_y)



def gen_pic(gen,flam_list,off_y):
    gen.read_flam(flam_list)

    gen_ram_mat(gen)
    gen_clock_mat(gen)
    gen_display_mat(gen)

    place_ram(gen,off_y)
    place_pow(gen,0,off_y,-7,0,gen.flam_number//7+2)
    place_clock(gen,off_y)
    place_display(gen,off_y)
    for y in range(0,gen.y_size):
        if y%7 == 0:
            place_pow(gen,5,-y+off_y,7,0,gen.x_size//7+1)




def gen_all(flam_list,p1):
    gen = gen_class()
    if len(flam_list) == 1:
        gen_pic(gen,flam_list[0],0)
    if len(flam_list) == 2:
        gen_pic(gen,flam_list[1],0)
        gen_pic(gen,flam_list[0],-32)
    if len(flam_list) == 3:
        gen_pic(gen,flam_list[2],0)
        gen_pic(gen,flam_list[1],-32)
        gen_pic(gen,flam_list[0],-64)

    
    pack_dir(gen)
