#! python3
import pyautogui, time
from tkinter import *
import threading
import random


def thread_it(func):
    '''将函数打包进线程'''
    # 创建
    t = threading.Thread(target=func)
    # 守护 !!!
    t.setDaemon(True)
    # 启动
    t.start()
    # 阻塞--卡死界面！
    # t.join()


def stop():
    exit(1)


def start():
    print('开始')
    tempposition = 0
    count = 0
    countTotal = int(w.get())
    mindUse = var2.get()
    esTime = int(estiBox.get())
    while count < countTotal:
        time.sleep(0.5)
        try:
            tempposition = findplay()
        except:
            pass
        time.sleep(1)
        # 寻找理智界面
        try:
            okPosition = pyautogui.locateCenterOnScreen('OK.png')

            if mindUse:
                pyautogui.click(okPosition)
            else:
                exit(1)
        except:
            pass

        try:
            count = findBegin(count, esTime, countTotal)

        except:
            pass

        if tempposition != 0:
            pyautogui.click(tempposition)
        if count == countTotal:
            exit(2)


def findplay():
    playposition = pyautogui.locateCenterOnScreen('playkey.png')
    pyautogui.click(playposition)
    return playposition


def findBegin(count, esTime, countTotal):
    opposition = pyautogui.locateCenterOnScreen('opstart.png')
    pyautogui.click(opposition)
    count = count + 1
    left = countTotal - count
    print('正在开始第', count, '次', '剩余', left)
    time.sleep(esTime)
    return count


def findMind(use):
    print('使用理智' + use)
    okPosition = pyautogui.locateCenterOnScreen('OK.png')
    if use == True:
        print('进入循环')
        pyautogui.click(okPosition)
    else:
        exit(1)


root = Tk()
root.geometry('540x320')
root.title('明日方舟自动模块')
estiTime = Label(root, text='预估一场时间（秒）',
                 width=20,
                 height=2,
                 )
estiTime.pack()

estivar = StringVar()
estivar.set('60')
estiBox = Entry(root, textvariable=estivar)
estiBox.pack()

mindlb = Label(root, text='是否自动使用理智',
               width=20,
               height=2,
               )
mindlb.pack()
var2 = BooleanVar()
rd1 = Radiobutton(root, text="是", variable=var2, value=True)
rd1.pack()

rd2 = Radiobutton(root, text="否", variable=var2, value=False)
rd2.pack()

timelb = Label(root, text='循环次数',
               width=20,
               height=2,
               )

timelb.pack()
timevar = StringVar()
# scl = Scale(root, orient=HORIZONTAL, length=200, from_=0, to=50, label='请拖动滑块', tickinterval=5, resolution=1,
#            variable=timevar)
# scl.pack()
w = Entry(root, textvariable=timevar)
w.pack()

btn1 = Button(root, text='启动', command=lambda: thread_it(start))
btn1.pack()

btn2 = Button(root, text='停止', command=stop)
btn2.pack()
root.mainloop()
