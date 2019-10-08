fi=open("history.ama","r",encoding="utf8")
sum=0
while True:
    data = fi.readline()
    if not data:
        break
    print(data,end="")
    #한줄 안에서 이름 가격 ...자르기
    l=data.split()          #(화이트스페이스) \t나 \n 띄어쓰기 있는걸 다 자름 . 빈공간 다 자르기
    sum += int(l[1])        #음료의 가격 합계를 구한다.
    #총 금액 계산하고, 출력하기
print("총 금액:"+str(sum)+"원")

fi.close()
