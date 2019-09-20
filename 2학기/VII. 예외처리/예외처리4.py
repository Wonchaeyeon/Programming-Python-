#p127

l=[1,2,3]
try:
    print(l[1])
    print(l[2])
    # print(l[4])   #IndexError: List index out of range
except IndexError as e:
    print("인덱스 에러")
    print(e)
else:    #else에러는 에러가 안나도 여기서 걸림, 에러가 except에서 걸리면 얘는 실행 안함
    print("성공적으로 모든 코드를 실행")
