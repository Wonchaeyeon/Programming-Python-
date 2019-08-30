# 전화번호부

Tel={"강은서":"010-4202-7249", "양수빈":"010-1111-2222", "윤수빈":"010-2222-3333",
    "원채연":"010-4069-8091","원채린":"010-4094-8091","권향숙":"010-5774-9153","원덕수":"010-3358-8091",
    "원세연":"010-4811-8091"}

name=input("이름을 입력하세요. : ")
for i in Tel:
  if name in i:
    print(i+" : "+Tel[i])


#import time
# import os
# words=['apple','banana','cherry']
# for word in words:
#     os.system()