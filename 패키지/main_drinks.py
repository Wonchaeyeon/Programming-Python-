# from foods.drinks import milk   #import는 모듈 또는 함수명이 가능하다.
# milk.drink()

# from foods.drinks.milk import drink     #임폴트뒤 쓴거는 무조건 본문에 나와야함.
# drink()

# import foods.drinks.milk
# foods.drinks.milk.drink()


# import foods.drinks.milk   #임폴트를 다쓰면 다 붙여줘야되긴 하는데 가능. 
# foods.drinks.milk.drink()

#foods.drinks.milk.drink()  #error


#from:폴더or모듈
#import:모듈 or 함수


from foods.drinks import milk as m
m.drink()
