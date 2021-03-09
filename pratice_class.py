class Unit():
    def __init__(self):
        print("유닛 생성자")

class Flyable:
    def __init__(self):
        print("flyable 생성자")

# class FlyableUnit(Unit, Flyable):
#     def __init__(self):
#         super().__init__() # 유닛 생성자   

# class FlyableUnit( Flyable,Unit ):
#     def __init__(self):
#         super().__init__()  # flyable 생성자

class FlyableUnit( Flyable,Unit ):
    def __init__(self):
        super().__init__()  # flyable 생성자
        Unit.__init__(self) # 이렇게 해야 둘 다 생긴다~~

dropship = FlyableUnit()