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



fp = open('errorLog.txt','a')
stderr = sys.stderr
sys.stderr = fp



num_dir = {
    '32*32(可用)': 32,
    '64*64(只浏览)': 64,
    '128*128(只浏览)': 128,
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
    resize = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)
    img_rgb = cv2.cvtColor(resize, cv2.COLOR_BGR2RGB)
    img = Image.fromarray(img_rgb)
    tkImage = ImageTk.PhotoImage(image=img)
    return tkImage


class Main_window():
    def __init__(self):
        self.flam_list = []
        self.window = tk.Tk()
        self.window.title('动图转蓝图 V0.1')
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
        numberChosen['values'] = ('32*32(可用)', '64*64(只浏览)', '128*128(只浏览)',
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
                      to=254,
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
        self.vSpeed.set(10)
        self.progress = tk.IntVar()
        self.progress.set(self.vStart.get())

    def up_img(self):
        self.cnt = self.progress.get()
        gray = cv2.cvtColor(self.flam_list[self.cnt], cv2.COLOR_BGR2GRAY)
        ret, im_fixed = cv2.threshold(gray, self.v1.get(), 255,
                                      cv2.THRESH_BINARY)
        dst = cv2.bitwise_not(im_fixed)
        n = num_dir[self.number.get()]
        size = (n, n)
        dst = cv2.resize(dst, size)
        tkImage = show_tkimg(dst, 300)
        self.label_img.configure(image=tkImage)
        self.label_img.image = tkImage
        self.cnt += 1
        if self.cnt >= self.vEnd.get():
            self.cnt = self.vStart.get()
        self.progress.set(self.cnt)
        self.window.after(35 - self.vSpeed.get(), lambda: self.up_img())

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
                      to=20,
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

    def start_go(self):
        if self.event._flag  == False:
            self.event.set()
            t = threading.Thread(target=self.th_go)
            t.setDaemon(True)
            t.start()
            self.wait_finish()

    def wait_finish(self):
        if self.event._flag == False :
            print('finish')
            self.event.clear()
            sl2 = tk.Toplevel()
            nameEntered = ttk.Entry(sl2, width=50, textvariable=self.text)   
            nameEntered.pack()
            return 0
        else:
            self.window.after(100,self.wait_finish)

    def th_go(self):
        fl_list = []
        for i in range(self.vStart.get(),self.vEnd.get()):
            gray = cv2.cvtColor(self.flam_list[self.cnt], cv2.COLOR_BGR2GRAY)
            ret, im_fixed = cv2.threshold(gray, self.v1.get(), 255,
                                      cv2.THRESH_BINARY)
            dst = cv2.bitwise_not(im_fixed)
            n = num_dir[self.number.get()]
            size = (n, n)
            dst = cv2.resize(dst, size)
            fl_list.append(dst)
        gen_all(fl_list)
        self.event.clear()


m_wd = Main_window()
m_wd.window.mainloop()
fp.close()
tp.cleanup()