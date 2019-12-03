#PyAutoGUI 설치
#pip install pyautogui

import pyautogui as pag
import time


if __name__ == '__main__':
     # while True:
     #     x,y=pag.position()
     #     print("x:{}\ty:{}".format(x,y), end="\r")
    # pag.moveTo(166,44,duration=2) #~까지 이동
    # pag.move(100,200,duration=2)  #~만큼 이동
    # pag.click()
    # pag.click()
    # pag.doubleClick() #더블클릭
    # pag.click(clicks=2)   #더블클릭
    # pag.drag(0,200,duration=1)    #드래그 duration있어야 함. 
    # pag.rightClick()  #오른쪽 버튼 
    # pag.click(484,44, dutation=1)
     pag.doubleClick(166,44,duration=2)
    #TODO:scroll
     time.sleep(1)  #크롬이 열리기를 기다려야힘.
     pag.typewrite("http://ticket.interpark.com/")
     pag.press("enter")
     # pag.press("hangul")  #한/영키 
     # pag.typewrite("dkdldb")  #아이유 영어로    
     # pag.press("enter")   
