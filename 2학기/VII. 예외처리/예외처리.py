l = [1,2,3]
try:
    print(l[2])
    print(1[3])     #indexError
except:
    print("리스트의 요소에 접근하지 못했습니다")
    