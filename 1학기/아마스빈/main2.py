from order import order
from file_manager2 import FileManager

#주문내역 불러오고, 출력하자
file_manager=FileManager("history.bin")
history = file_manager.load()
# if len(history)==0:
#     print("주문내역이 없습니다.")
# else:
sum=0
for h in history:          #들여쓰기 앞으로 댕기기 (shift+Tab)
    print(h)
    sum += h.price
print("내가 아마스빈에 갖다 바친 돈: "+str(sum)+"원")



#지금 주문하자
o=order()
o.order_drink()

#주문내역 저장하자
file_manager.save(history+o.order_menu)
