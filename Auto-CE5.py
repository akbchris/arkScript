#! python3
import pyautogui, time
from tkinter import *
import threading


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
    print('start')
    tempposition = 0
    count = 0
    countTotal = scl.get()
    use = var.get()
    print(use)
    while count < countTotal:
        time.sleep(0.5)
        try:
            tempposition = findplay()
        except:
            pass
        time.sleep(0.5)

        try:
            count = findBegin(count)
            left = countTotal - count
            print('正在开始第', count, '次', '剩余', left)
        except:
            pass

        if tempposition != 0:
            pyautogui.click(tempposition)


def findplay():
    playposition = pyautogui.locateCenterOnScreen('playkey.png')
    pyautogui.click(playposition)
    return playposition


def findBegin(count):
    opposition = pyautogui.locateCenterOnScreen('opstart.png')
    pyautogui.click(opposition)
    count = count + 1
    time.sleep(60)
    return count


def findMind(use):
    print('使用理智' + use)
    print(pyautogui.locateCenterOnScreen('mm.png'))
    if use == True:
        print('进入循环')
    else:
        exit(1)


root = Tk()
root.geometry('540x320')
root.title('明日方舟自动模块')
mindlb = Label(root, text='是否使用理智',
               width=20,
               height=2,
               )
mindlb.pack()

var = BooleanVar()
rd1 = Radiobutton(root, text="是", variable=var, value=True)
rd1.pack()

rd2 = Radiobutton(root, text="否", variable=var, value=False)
rd2.pack()

timelb = Label(root, text='循环次数',
               width=20,
               height=2,
               )

timelb.pack()
timevar = IntVar()
scl = Scale(root, orient=HORIZONTAL, length=200, from_=0, to=50, label='请拖动滑块', tickinterval=5, resolution=1,
            variable=timevar)
scl.pack()

btn1 = Button(root, text='启动', command=lambda: thread_it(start))
btn1.pack()

btn2 = Button(root, text='停止', command=stop)
btn2.pack()
root.mainloop()
