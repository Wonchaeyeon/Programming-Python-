import pyautogui as pag
import time


if __name__ == '__main__':
    data=pag.locateOnScreen("크롬.png")
    print(data)
    #pag.moveTo(112+(109/2),7+(105/2),duration=2)
    #pag.moveTo(data.left+(data.width/2),date.top+(data.height/2))
    # center=pag.center(data)
    # print(center)
    # center=pag.locateCenterOnScreen("크롬.png")
    # pag.moveTo(center,duration=2)
    # pag.doubleClick()
    datas=pag.locateAllOnScreen("크롬.png")   #특정 이미지 모두 가져와서 위치 찍기
    for dat in datas:
        print(data)