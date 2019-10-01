fi=open("history.ama","r",encoding="utf8")

while True:
    data = fi.readline()
    if not data:
        break
    print(data,end="")
    #한줄 안에서 이름 가격 ...자르기
    #총 금액 계산하고, 출력하기

fi.close()
