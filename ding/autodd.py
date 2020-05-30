import pyautogui
from time import sleep
import pyperclip
def auto():
    def vartual():
        #打开虚拟机
        pyautogui.moveTo(x=0,y=494,duration=0.3)
        sleep(1)
        a,b = pyautogui.locateCenterOnScreen('mumu.png',grayscale=False,confidence = 0.8)
        pyautogui.leftClick(x=a/2, y=b/2)
        #等待
        sleep(6)
        #打开钉钉
        while True:
            try:
                a,b = pyautogui.locateCenterOnScreen('dingding.png',grayscale=False,confidence = 0.9)
                pyautogui.leftClick(x=a / 2, y=b/ 2)
            except TypeError:
                sleep(1)
                continue
            break

        #打开签到窗口
        sleep(2)
        while True:
            try:
                a,b = pyautogui.locateCenterOnScreen('2017.png',grayscale=False,confidence = 0.9)
                pyautogui.leftClick(x=a / 2, y=b/ 2)
            except TypeError:
                sleep(1)
                continue
            break
    def motion():
        i = 60
        while i>0:
            pyautogui.scroll(-10)
            i -=1
    def questionare():
        while True:
            try:
                a,b = pyautogui.locateCenterOnScreen('notnow.png',grayscale=False,confidence = 0.9)
                pyautogui.leftClick(x=a / 2, y=b/ 2)
            except TypeError:
                pass
            break
        while True:
            try:
                a,b = pyautogui.locateCenterOnScreen('ignore.png',grayscale=False,confidence = 0.7)
                pyautogui.leftClick(x=a / 2, y=b/ 2)
            except TypeError:
                pass
            break
        sleep(2)

        while True:
            try:
                a, b = pyautogui.locateCenterOnScreen('health.png', grayscale=False, confidence=0.7)
                pyautogui.leftClick(x=a / 2, y=b / 2)
            except TypeError:
                sleep(1)
                continue
            break

        # heath

        sleep(2)

        while True:
            try:
                a,b = pyautogui.locateCenterOnScreen('today.png',grayscale=True,confidence = 0.7)
                pyautogui.leftClick(x=a / 2, y=b/ 2)
            except TypeError:
                sleep(1)
                continue
            break


        sleep(2)
        try:
            a, b = pyautogui.locateCenterOnScreen('cancel.png', grayscale=False, confidence=0.7)
            pyautogui.leftClick(x=a / 2, y=b / 2)
        except TypeError:
            pass
        sleep(2)
        motion()
        sleep(1)
        a, b = pyautogui.locateCenterOnScreen('submit.png', grayscale=False, confidence=0.7)
        pyautogui.moveTo(x=a / 2, y=b / 2)
        pyautogui.leftClick(x=a / 2, y=b / 2)
        sleep(1.5)
        #返回
        a, b = pyautogui.locateCenterOnScreen('back.png', grayscale=False, confidence=0.6)
        pyautogui.leftClick(x=a/2-10,y=b/2+10)
        sleep(1.5)
        a, b = pyautogui.locateCenterOnScreen('quit.png', grayscale=False, confidence=0.6)
        pyautogui.leftClick(x=a / 2, y=b / 2)
    def sign():

        try:
            a, b = pyautogui.locateCenterOnScreen('sign.png', grayscale=True, confidence=0.6)
            pyautogui.leftClick(x=a / 2, y=b / 2)
        except TypeError:
            a, b = pyautogui.locateCenterOnScreen('sign.png', grayscale=True, confidence=0.8)
            pyautogui.leftClick(x=a / 2, y=b / 2)
        sleep(.5)
        a, b = pyautogui.locateCenterOnScreen('DING.png', grayscale=False, confidence=0.9)
        pyautogui.leftClick(a/2,b/2+70)
        pyautogui.dragTo(a/2-100,b/2+70,button='left')
        pyautogui.dragTo(a/2-200,b/2+70,button='left')
        a, b = pyautogui.locateCenterOnScreen('signin.png', grayscale=False, confidence=0.9)
        pyautogui.leftClick(x=a / 2, y=b / 2)
        sleep(3)

        try:
            a, b = pyautogui.locateCenterOnScreen('donotsign.png', grayscale=False, confidence=0.6)
            pyautogui.leftClick(x=a / 2, y=b / 2)
        except TypeError:
            pass
        a, b = pyautogui.locateCenterOnScreen('final_sign.png', grayscale=False, confidence=0.9)
        pyautogui.moveTo(x=a / 2, y=b / 2)
        pyautogui.leftClick(x=a / 2, y=b / 2)
        sleep(1)
        quit()
    def quit():
        pyautogui.hotkey('command','q')
    def send1():
        str1 = ('1 家中无体温计，自测体温正常')
        a, b = pyautogui.locateCenterOnScreen('find.png', grayscale=True, confidence=0.7)
        pyautogui.leftClick(x=a / 2, y=b / 2)
        pyautogui.write('1049879290')
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        pyperclip.copy(str1)
        sleep(2)
        a, b = pyautogui.locateCenterOnScreen('chat.png', grayscale=True, confidence=0.5)
        pyautogui.leftClick(x=a / 2, y=b / 2)
        pyautogui.hotkey('command', 'v')
        pyautogui.hotkey('enter')
        sleep(1)
    def send2():
        str2 = ('对接宿舍已完成')
        a, b = pyautogui.locateCenterOnScreen('find.png', grayscale=True, confidence=0.7)
        pyautogui.leftClick(x=a / 2, y=b / 2)
        pyautogui.write('1048110013')
        sleep(1)
        pyautogui.press('enter')
        sleep(1)
        pyperclip.copy(str2)
        sleep(2)
        a, b = pyautogui.locateCenterOnScreen('chat.png', grayscale=True, confidence=0.5)
        pyautogui.leftClick(x=a / 2, y=b / 2)
        pyautogui.hotkey('command', 'v')
        pyautogui.hotkey('enter')
        sleep(1)
    def QQ():
        #打开QQ
        pyautogui.moveTo(x=0,y=494,duration=0.3)
        sleep(3)
        try:
            a,b = pyautogui.locateCenterOnScreen('QQ.png',grayscale=False,confidence = 0.7)
            pyautogui.leftClick(x=a/2, y=b/2)
            sleep(1)
            pyautogui.hotkey('enter')
            sleep(5)
            a, b = pyautogui.locateCenterOnScreen('find.png', grayscale=False, confidence=0.7)
            pyautogui.leftClick(x=a / 2, y=b / 2)
        except TypeError:
            a, b = pyautogui.locateCenterOnScreen('find.png', grayscale=True, confidence=0.6)
            pyautogui.leftClick(x=a / 2, y=b / 2)
        send1()
        send2()
        quit()
    def dingding():
        vartual()
        questionare()
        sign()
        quit()
    dingding()
    QQ()
if __name__== '__main__':
    auto()
