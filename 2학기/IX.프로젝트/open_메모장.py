import pyautogui as pag
import time

if __name__ == '__main__':
    #메모장 프로그램 실행하자
    #pag.moveTo(109, 1045, duration=2)
    pag.press("winleft")
    #pag.doubleClick()
    pag.press("hangul")
    time.sleep(2)
    pag.typewrite("apahwkd")
    pag.press("enter")
    #hello world 치자
    time.sleep(2)
    pag.typewrite("HelloWorld")
    #두 줄 내리자
    pag.press("enter",2)
    #반갑구나 세상아 치자
    pag.press("hangul")
    pag.typewrite("qksrkqrnsk tptkddk")
    #helloworld로 저장하자
    pag.hotkey("Ctrl", "s")
    time.sleep(2)
    pag.typewrite("helloworld")
    pag.press("hangul")
    pag.press("enter")


