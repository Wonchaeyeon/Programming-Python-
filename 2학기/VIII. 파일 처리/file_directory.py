import os

data=os.listdir(".")  #상대경로, 현재 디렉터리
# print(data)
for d in data:
    print(d)
    print("is dirrectory?: "+str(os.path.isdir(d)))
    print("is file?: "+str(os.path.isfile(d)))