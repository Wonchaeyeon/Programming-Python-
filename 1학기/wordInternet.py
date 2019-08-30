import random

class confuse:
    __dic = {
        "apple":"사과","airplane":"비행기","zoo":"동물원",
        "beauty":"미인","handsome":"잘생긴","monster":"괴물",
        "sun":"태양","test":"연습, 실험","level":"단계",
        "human":"사람","rock":"바위","love":"사랑",
        "lover":"연인","classic":"오래된, 고전의","mouse":"쥐"
        }
    __list = []

    def __init__(self):
        self.__list = []
        
        for x in self.__dic:
            self.__list.append(x)

    def printlist(self):
        return self.__list

    def insertword(self,word,detail):
        self.__dic[word] = detail
        
        self.__list = []
        
        for x in self.__dic:
            self.__list.append(x)

    def searchword(self,word):
        try:
            searchValue = self.__dic[word]
        except KeyError:
            return "NULL"
        else:
            return searchValue

    def chooseword(self):
        random.shuffle(self.__list)
        string = self.__list[0]
        strlist = []
        for x in string:
            strlist.append(x)
        random.shuffle(strlist)

        strshuffle = ""
        for x in strlist:
            strshuffle += x

        return [strshuffle,string,self.__dic[string]]

    def delword(self,word):
        del self.__dic[word]

        self.__list=[]
        for x in self.__dic:
            self.__list.append(x)

game = confuse()
while 1:
    print ("\n\n===== !Confuse! =====")
    print ("SELECT ---> 1. START")
    print ("            2. INSERT")
    print ("            3. PRINT")
    print ("            4. DELETE")
    print ("            0. EXIT")
    print ("=====================")

    sel = raw_input(" >")
    print ("")

    if(sel == "1"):
        exam = game.chooseword()
        print ("===== EXAM =====".center(20))
        print exam[0].center(20)
        print ("================".center(20))
        print exam[2].center(20)
        print ("================".center(20))
        tt = raw_input("답 >")

        print ""
        if(tt == exam[1]):
            print ("정답!!")
        else:
            print ("오답!!")
    elif(sel == "2"):
        t1 = raw_input("영 단어 : ")
        t2 = raw_input("뜻 : ")

        if(game.searchword(t1) != "NULL"):
            print ("입력된 단어입니다.")
        else:
            print ("단어를 입력합니다.")
            game.insertword(t1,t2)
    elif(sel == "3"):
        print game.printlist()
    elif(sel == "4"):
        tt = raw_input("지울 단어 : ")

        if(game.searchword(tt) == "NULL"):
            print ("지울 단어는 없습니다.")
        else:
            print ("단어를 지웁니다.")
            game.delword(tt)
        
    elif(sel == "0"):
        print ("게임을 끝냅니다.")
        break


#출처: https://maks.tistory.com/entry/Python으로-만드는-간단한-영어-단어-맞추는-게임 [막장인생의 막장 스토리]