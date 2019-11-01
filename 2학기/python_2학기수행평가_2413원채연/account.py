import pickle
class Account:     #개인 계좌 관리
    def __init__(self):
        self.user = input("계좌번호=")
        self.name=input("고객이름=")
        self.balance=input("예금금액=")

    def disp(self):  #입금
        print("{0} :{1} :{2}".format(self.user,self.name,self.balance))
    def getid(self):
        return self.user
    def getBalance(self):
        return self.balance

class BankManager(Account):   #여러계좌관리

    def one_user(self,user):   #한 고객의 정보 얻기 위해
        userlist=""
        count=-1
        if self.check_user(user)==False:  #아이디 존재할 때
            try:
                f=open("account.txt","r")
            except FileNotFoundError as e:
                pass
            else:
                for line in f:
                    count += 1
                    if user == line.split(",")[0]:
                        userlist=line
                        break
            finally:
                f.close()
        return  count,userlist

    def check_user(self,user):   #계좌번호의 중복여부를 판단할 메소드

        check=True
        try:
            f = open("account.txt", "r")
            data=pickle.load(f)
        except FileNotFoundError as e:
            f=open("account.txt","w")
        else:
            for line in f:
                if user == line.split(",")[0]:  #아이디 중복되면 break
                    check = False
                    break
        finally:
            f.close()
        return check

    def makeAccount(self):
        print("\n=====계좌등록=====")
        super().__init__()
        super().disp()
        result = self.check_user(super().getid())

        print(result)

        if result:   #참일때 txt파일에 저장
            try:
                f=open("account.txt","a")
            except FileNotFoundError:   #파일 존재하지 않을때 새로 만들기
                f=open("account.txt","w")
            finally:
                f.write(self.user+","+self.name+","+self.balance+"\n")
                f.close()
        else:  #거짓일때 중복됐다고 알리기
            print("id가 중복됩니다. 다시 입력해 주세요")
        print("===================================")

    def showAccount(self):    #전체고객의 계좌정보를 출력할 메소드
        userlist=[]
        try:
            f=open("account.txt","r")
        except FileNotFoundError as e:
            print("고객이 없습니다.")
        else:
            for line in f:
                userlist.append(line)
        finally:
            f.close()
        return userlist

class BankingSystem(BankManager):
    num=0
    def __init__(self,num):
        self.num=int(num)

    def controler(self):
        if self.num==1:
            super().makeAccount()
        elif self.num==2:
            self.printdeposit()
        elif self.num==3:
            self.printwithdraw()
        elif self.num==4:
            self.printshow()

    def printwithdraw(self):    #출금처리 담당 메소드
        print("=======출금처리=======")
        user=input("계좌번호 : ")
        count,userlist= self.one_user(user)
        print("============================")
        if userlist != "":
            user,username,userbalance=userlist.split(',')
            print("{0} : {1} : {2} ".format(user,username,userbalance))
            print("============================\n")

            try:
                price=int(input("출금금액 :"))
            except ValueError as e:
                print("잘못입력하셨습니다")
            else:
                if(int(userbalance)-int(price))<0:
                    print("고객님 계좌의 잔액이 부족합니다.")
                else:
                    self.change_draw(user,username,int(userbalance)-price,count)
                    print("출금 처리가 완료되었습니다. ")
        else:
            print("일치하는 계좌번호가 존재하지 않습니다.")
        print("==============================")
    def chaenge_draw(self,user,username,userbalance,count):
        f=open("account.txt","r+")
        for i in range(0,count):
            f.readline()
        f.seek(f.tell(),0)
        f.writelines(user,+","+username+","+str(userbalance)+"\n")
        f.close()

    def change_deposit(self,user,username,userbalance,count):
        f=open("account.txt","r+")
        for i in range(0,count):
            f.readline()
        f.seek(f.tell(),0)
        f.writelines(user+","+username+","+str(userbalance)+"\n")

    def printdeposit(self):
        print("====입금처리====")     #입금처리 담당 메소드
        user=input("계좌번호 : ")
        count,userlist = self.one_user(user)
        print("=======================")
        if userlist != "":
            user,username,userbalance=userlist.split(',')
            print("{0}:{1}:{2}".format(user,username,userbalance))
            price=0
            print("=========================\n")
            try:
                price=int(input("입금금액 :"))
            except ValueError as e:
                print("잘못입력하셨습니다")
            else:
                self.change_deposit(user,username,int(userbalance)+price,count)
                print("입금처리가 완료되었습니다.")
        else:
            print("일치하는 계좌번호가 존재하지 않습니다.")
        print("===========================")

    def printshow(self):
        print("==== 전체고객 ====")    #전체고객 조회 메소드
        userlist=super().showAccount()
        for i in range(0,len(userlist)):
            a,b,c=userlist[i].split(",")
            print("{0}:{1}:{2}".format(a,b,c),end="")
        print("=========================")

if __name__=="__main__":
    while True:
        print("=== Bank Manu ====")
        print("1. 계좌개설")
        print("2. 입금처리")
        print("3. 출금처리")
        print("4. 전체고객 잔액현황")
        print("5. 프로그램 종료")
        print("=======================")
        try:
            num=int(input("선택 : "))
        except ValueError as e:
            print("잘못입력하셨습니다.")

        else:
            if num == 5:
                break
            else:
                b=BankingSystem(num)
                b.controler()









