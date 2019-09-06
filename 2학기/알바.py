#일주일에 얼마나 일했는지, 몇 주 일하는지, 시급 얼마인지 입력하면 총 알바비 계산
#주 15시간 이상하면 주휴수당 지급( 주휴수당은 5일 일한 것에 1일차 급여 더 지급)

minu=int(input("일주일에 몇 시간 일 했나요?"))
week=int(input("몇 주 일하셨나요?"))
pay=int(input("시급이 얼마에요?"))

Albamoney=(pay*minu*week)
print("총 알바비는:{0}원 입니다.".format(Albamoney))
