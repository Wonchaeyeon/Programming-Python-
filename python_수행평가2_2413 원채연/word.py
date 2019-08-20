kor = ["사과", "아버지", "학교", "책상", "남자"] 
eng = ["apple", "father", "school", "desk", "man"] 

score = 0   #점수 계산 변수

def word():   #단어와 뜻을 보여주고, 입력하는 함수
    global ans
    print("한글 : " + kor[i])
    ans = input("영어 : ") 

for i in range(5):    #5개까지 
    word()
    for j in range(1):

        if ans.lower() == eng[i]: 
            print("참 잘했어요!\n")
            score = score + 1

        else: #10

            if ans.lower() != eng[i]: 
                print(kor[i]+"는(은) "+eng[i]+"입니다.")
                print()
            
            else:     
                print("틀렸어요! 다시하세요!")
                print()
                word()

print("정답 갯수 :", score)