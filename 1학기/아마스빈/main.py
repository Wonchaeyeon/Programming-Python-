#아마스빈 주문앱
    #Drink <-Coffee
    #       <-Bubbletea
    #Order
    #메뉴 보여주자
    #음료주문하자
    #주문한 음료 보여주자
    #총금앱 계산하자
    # 1. 음료 이름 가격
    # 2. 컵 사이즈 레귤러 점보
    # 3. 얼음량 0,50,100,150
    # 4. 당도 0,50,100,150
    # 5. 펄 타피오카, 코코,젤리, 알로에

from order import order
from file_manager import FileManager


#주문내역 불러오고 보여주자

file_manager=FileManager("history.bin")
# answer = input("주문내역을 볼까요?(y or n)")
# if answer == "y":
history=[]
try:
    history=file_manager.load()
    sum=0
    for h in history:
        print(h)
        sum += h.price
    print("여태까지 내가 아마스빈에 쏟아부은 돈: "+str(sum)+"원")
except FileNotFoundError:
    print("주문 내역이 없습니다.")

o =order()
o.order_drink()

#주문내역 저장하자
file_manager.save(history+o.order_menu)
   