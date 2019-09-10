#버스 여유, 보통, 혼잡
#탑승객, 하차객 입력받자
#0명 이상 10 미만 : 여유, 10명이상 20명 미만: 보통, 20이상: 혼잡

sum=0

#--------반복하기
while True:
    inn=input("탑승객 수는?: (-1: 끝): ")
    if inn == "-1":
        break
    inn = int(inn)
    out = int(input("하차객 수는?:"))
    sum += inn-out

#----

print("버스에 있는 사람수는",sum)

if 0 <= sum < 10:
    print("[[여유]]")
elif 10 <= sum <20:
    print("[[보통]]")
else:
    print("[[혼잡]]")