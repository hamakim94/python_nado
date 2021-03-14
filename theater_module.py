# 모듈 : 부품처럼 사용한다, 확장자는 .py

# 극장이 있다고 가정, 현금만 받아.. 잔돈을 안바꿔줘

# 일반 가격 정보를 반환

def price(people):
    print("{0}명 가격은 {1}원 입니다".format(people, people*10000))

# 조조할인 가격

def price_morning(people):
    print("{0}명 조조할인 가격은 {1}원 입니다".format(people, people*6000))

# 군인할인

def price_soldier(people):
    print("{0}명 군인할인 가격은 {1}원 입니다".format(people, people*4000))
