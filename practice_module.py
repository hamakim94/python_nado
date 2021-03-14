# import theater_module

# theater_module.price(3) # 3명이서 영화보러 갔을 때 가격..
# theater_module.price_morning(4) # 4명이서 조조할인 영화보러 갔을 때 
# theater_module.price_soldier(5) # 5명의 군인이 영화보러 갈 떄 

# import theater_module as mv # 별명 붙여주기

# mv.price(3)

# from theater_module import * # from random import &

# price(3)
# price_soldier(5)
# price_morning(4)

# from theater_module import price, price_morning # 군전역함, 이제 필요 없어

# price(5)
# price_morning(6)
# # price_soldier(3) # NameError: name 'price_soldier' is not defined

from theater_module import price_soldier as price # 이거, 1개만 가능
price(5) # 모듈에 정의된 price와는 달라~


