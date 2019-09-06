#국어, 영어, 수학, 자바, 파이썬, JSP 점수 입력받기
#총점, 평균 구하기
#용돈 구하기 90점이상 : 10만원, 80점 이상 : 8만원, 70점 이상: 7만원, 60점 이상 : 6만원, 그 미만 : 5만원

k=int(input("국어 점수를 입력하세요: "))
e=int(input("영어 점수를 입력하세요: "))
m=int(input("수학 점수를 입력하세요: "))
ja=int(input("자바 점수를 입력하세요: "))
p=int(input("파이썬 점수를 입력하세요: "))
jsp=int(input("JSP 점수를 입력하세요: "))

sum=(k+e+m+ja+p+jsp)
avg=(sum/6)

print("총점은:",sum,"평균은:",round(avg,2))

if avg >=90: 
    print("용돈 10만원")
elif avg >=80:
    print("용돈 8만원")
elif avg >= 70:
    print("용돈 7만원")
elif avg >=60:
    print("용돈 6만원")
elif avg >50:
    print("용돈 5만원")
else:
    print("용돈 5만원입니당")

