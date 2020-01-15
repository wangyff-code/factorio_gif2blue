import tkinter as tk
from tkinter import filedialog, ttk

import cv2
import numpy as np
from PIL import Image, ImageTk

import sys
import  threading 

import time
import tempfile
import os
from shutil import copyfile
from trans_fun import gen_all




tp = tempfile.TemporaryDirectory()

np.set_printoptions(threshold=np.inf)

fp = open('errorLog.txt','a')
stderr = sys.stderr
sys.stderr = fp



num_dir = {
    '32*32(可用)': 32,
    '64*64(可用)': 64,
    '96*96(可用)': 96,
    '128*128(可用)': 128,
    '160*160(可用)': 160,
    '256*256(只浏览)': 256,
    '512*512(只浏览)': 512
}



def show_tkimg(img, zoon):
    x, y = img.shape[0:2]
    t = max(x, y)
    t = (zoon / t)
    x *= t
    y *= t
    dim = (int(y), int(x))
    # resize = cv2.resize(img,dim)
    img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img_rgb)
    img = img.resize(dim)
    tkImage = ImageTk.PhotoImage(image=img)
    return tkImage


class Main_window():
    def __init__(self):
        self.flam_list = []
        self.window = tk.Tk()
        self.window.title('GIF转蓝图V1.4.1')
        self.event = threading.Event()
        self.fm1 = tk.Frame(self.window)
        self.fm1 = tk.Frame(self.window)
        menubar = tk.Menu(self.window)
        fmenu1 = tk.Menu(self.window)
        for item in ['打开']:
            fmenu1.add_command(label=item, command=lambda: self.openfiles())
        fmenu2 = tk.Menu(self.window)
        for item in ['高级设置']:
            fmenu2.add_command(label=item, command=lambda: self.set_adv())
        menubar.add_cascade(label="文件", menu=fmenu1)
        menubar.add_cascade(label="设置", menu=fmenu2)
        self.window['menu'] = menubar

        start_img = np.zeros((300,300),dtype=np.uint8)
        img = Image.fromarray(start_img)
        tkImage = ImageTk.PhotoImage(image=img)
        self.label_img = tk.Label(self.fm1, image=tkImage)
        self.label_img.pack(side=tk.LEFT)
        self.label_img.configure(image=tkImage)
        self.label_img.image = tkImage

        self.fm1.pack()

        f2 = tk.Frame(self.window)
        self.number = tk.StringVar()
        numberChosen = ttk.Combobox(f2,
                                    width=10,
                                    height=10,
                                    textvariable=self.number)
        numberChosen['values'] = ('32*32(可用)', '64*64(可用)', '96*96(可用)','128*128(可用)','160*160(可用)',
                                  '256*256(只浏览)', '512*512(只浏览)')
        numberChosen.grid(column=1, row=1)
        numberChosen.current(0)
        numberChosen.pack()
        com = tk.Button(f2, text='高级选项', command=self.set_adv)
        com.pack()
        l = tk.Label(f2,
                     text="阈值下限",
                     bg="pink",
                     font=("Arial", 10),
                     width=7,
                     height=1)
        l.pack(side=tk.LEFT)
        self.v1 = tk.IntVar()
        s1 = tk.Scale(f2,
                      from_=0,
                      to=512,
                      length=800,
                      orient=tk.HORIZONTAL,
                      variable=self.v1)
        self.v1.set(100)
        s1.pack(side=tk.LEFT)
        f2.pack()

        f3 = tk.Frame(self.window)
        com = tk.Button(f3, text='开始转换', command=self.start_go)
        com.pack()
        self.p1 = ttk.Progressbar(f3,
                                  length=800,
                                  mode="determinate",
                                  orient=tk.HORIZONTAL)
        self.p1.pack()
        self.p1["maximum"] = 100
        self.p1["value"] = 0
        f3.pack()

        self.cnt = 0
        self.flm_len = 0
        self.ini_vluble()
        self.text = tk.StringVar()
    def openfiles(self):
        s2fname = filedialog.askopenfilename(title='打开文件',
                                             filetypes=[('gif', '*.gif'),
                                                        ('All Files', '*')])
        if len(s2fname) != 0:
            path,tepname = os.path.split(s2fname)
            temp_f = tp.name+'/'+tepname
            copyfile(s2fname,temp_f)
            cap = cv2.VideoCapture(temp_f)
            self.flam_list = []
            self.cnt = 0
            while True:
                ret, frame = cap.read()
                if ret == True:
                    self.flam_list.append(frame)
                else:
                    break
            self.flm_len = len(self.flam_list)

            self.ini_vluble()
            self.up_img()

    def ini_vluble(self):
        self.vStart = tk.IntVar()
        self.vStart.set(0)
        self.vEnd = tk.IntVar()
        self.vEnd.set(self.flm_len)
        self.vSpeed = tk.IntVar()
        self.vSpeed.set(20)
        self.progress = tk.IntVar()
        self.progress.set(self.vStart.get())
        self.divid = tk.IntVar()
        self.divid.set(2)

    def up_img(self):
        self.cnt = self.progress.get()
        im_fixed = self.do_img(self.cnt)

        tkImage = show_tkimg(im_fixed, 300)
        self.label_img.configure(image=tkImage)
        self.label_img.image = tkImage
        self.cnt += 1
        if self.cnt >= self.vEnd.get():
            self.cnt = self.vStart.get()
        self.progress.set(self.cnt)
        self.window.after(175 - self.vSpeed.get(), lambda: self.up_img())

    def do_img(self,cnt):
        gray = cv2.cvtColor(self.flam_list[cnt], cv2.COLOR_BGR2GRAY)

        dst = cv2.bitwise_not(gray)
        n = num_dir[self.number.get()]
        size = (n, n)
        dst = cv2.resize(dst, size)
        if self.v1.get() <=255:
            ret, im_fixed = cv2.threshold(dst, self.v1.get(), 255,
                                      cv2.THRESH_BINARY)
            im_fixed = cv2.bitwise_not(im_fixed)
        else:
            ret, im_fixed = cv2.threshold(dst, 512-self.v1.get(), 255,
                                      cv2.THRESH_BINARY)

        return im_fixed

    def set_adv(self):
        self.sl1 = tk.Toplevel()
        f2 = tk.Frame(self.sl1)



        l = tk.Label(f2,
                     text="开始位置",
                     bg="pink",
                     font=("Arial", 10),
                     width=7,
                     height=1)
        l.grid(column=0, row=0)
        s1 = tk.Scale(f2,
                      from_=0,
                      to=self.flm_len,
                      length=800,
                      orient=tk.HORIZONTAL,
                      variable=self.vStart)
        s1.grid(column=1, row=0)

        l = tk.Label(f2,
                     text="结束位置",
                     bg="pink",
                     font=("Arial", 10),
                     width=7,
                     height=1)
        l.grid(column=0, row=1)
        s1 = tk.Scale(f2,
                      from_=0,
                      to=self.flm_len,
                      length=800,
                      orient=tk.HORIZONTAL,
                      variable=self.vEnd)
        s1.grid(column=1, row=1)

        l = tk.Label(f2,
                     text="速度",
                     bg="pink",
                     font=("Arial", 10),
                     width=7,
                     height=1)
        l.grid(column=0, row=2)
        s1 = tk.Scale(f2,
                      from_=1,
                      to=170,
                      length=800,
                      orient=tk.HORIZONTAL,
                      variable=self.vSpeed)
        s1.grid(column=1, row=2)


        l = tk.Label(f2,
                     text="进度",
                     bg="pink",
                     font=("Arial", 10),
                     width=7,
                     height=1)
        l.grid(column=0, row=3)
        s1 = tk.Scale(f2,
                      from_=0,
                      to=self.flm_len,
                      length=800,
                      orient=tk.HORIZONTAL,
                      variable=self.progress)
        s1.grid(column=1, row=3)
        f2.pack()

        l = tk.Label(f2,
                     text="抽帧（N取1）",
                     bg="pink",
                     font=("Arial", 10),
                     width=7,
                     height=1)
        l.grid(column=0, row=4)
        s1 = tk.Scale(f2,
                      from_=1,
                      to=20,
                      length=800,
                      orient=tk.HORIZONTAL,
                      variable=self.divid)
        s1.grid(column=1, row=4)
        f2.pack()



    def start_go(self):
        if self.event._flag  == False:
            self.event.set()
            t = threading.Thread(target=self.th_go)
            t.setDaemon(True)
            t.start()
            self.wait_finish()

    def wait_finish(self):
        if self.event._flag == False :
            self.p1['value'] = 0
            os.startfile(r'blue_code.txt')
            self.event.clear()
            return 0
        else:
            self.window.after(100,self.wait_finish)

    def th_go(self):
        fl1_list = []
        fl2_list = []
        fl3_list = []
        fl4_list = []
        fl5_list = []
        for i in range(self.vStart.get(),self.vEnd.get()):
            im_fixed = self.do_img(i)
            x,y = im_fixed.shape
            if x == 32:
                if i%self.divid.get() == 0:
                    fl1_list.append(im_fixed)
            if x == 64:
                if i%self.divid.get() == 0:
                    flam1,flam2 = np.split(im_fixed,2,axis=0)
                    fl1_list.append(flam1)
                    fl2_list.append(flam2)
            if x == 96:
                if i%self.divid.get() == 0:
                    flam1,flam2,flam3 = np.split(im_fixed,3,axis=0)
                    fl1_list.append(flam1)
                    fl2_list.append(flam2)
                    fl3_list.append(flam3)
            if x == 128:
                if i%self.divid.get() == 0:
                    flam1,flam2,flam3,flam4 = np.split(im_fixed,4,axis=0)
                    fl1_list.append(flam1)
                    fl2_list.append(flam2)
                    fl3_list.append(flam3)
                    fl4_list.append(flam4)
            if x == 160:
                if i%self.divid.get() == 0:
                    flam1,flam2,flam3,flam4,flam5 = np.split(im_fixed,5,axis=0)
                    fl1_list.append(flam1)
                    fl2_list.append(flam2)
                    fl3_list.append(flam3)
                    fl4_list.append(flam4)
                    fl5_list.append(flam5)
        if x == 32:
            gen_all([fl1_list],self.p1)
        if x == 64:
            gen_all([fl1_list,fl2_list],self.p1)
        if x == 96:
            gen_all([fl1_list,fl2_list,fl3_list],self.p1)
        if x == 128:
            gen_all([fl1_list,fl2_list,fl3_list,fl4_list],self.p1)
        if x == 160:
            gen_all([fl1_list,fl2_list,fl3_list,fl4_list,fl5_list],self.p1)
        self.event.clear()


m_wd = Main_window()
m_wd.window.mainloop()
fp.close()
tp.cleanup()