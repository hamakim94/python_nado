chicken = 10
waiting = 1

class SoldOutError(Exception):
    pass

while(True):
    try:
        print("[남은 치킨 : {}]".format(chicken))
        order = int(input("치킨 몇마리 주문? "))
        if order < 1 :
            raise ValueError

        if order > chicken :
            print("재료가 부족합니다")
        else:
            print("[대기번호 {0}], {1}마리 주문이 완료됐습니다".format(waiting, order))
            waiting += 1
            chicken -= order
        if chicken == 0 :
            raise SoldOutError
    except ValueError:
        print("잘못된 값을 입력하셨습니다")
    except SoldOutError :
        print("재고가 소진돼 더이상 주문 안 받아")
        break
