#p127

l=[1,2,3]
try:
    print(l[4])   #IndexError: List index out of range
except IndexError as e:
    print("인덱스 에러")
    print(e)
