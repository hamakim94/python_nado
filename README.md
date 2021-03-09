# python_nado
youtube channel nadocoding

# 잘 몰랐던 것들(3/9)

## 1. Try, Except 사용자 정의
class SexyError(Exception): -> 사용자 정의 error 만들기
    pass

try: 
    if 뭐시기
        raise 내가정의
except (raise한 error):  ->이렇게하면 아무것도 안 일어남
    print("뭐시기")

## 2. class 상속 __init__활용
상속받은 class에서 __init__ 사용하려면 
부모클래스.__init__(self, 부모 클래스 변수들)


