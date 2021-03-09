class Unit: # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        
    def move(self, location):
        print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
            .format(self.name, location, self.speed))

class AttackUnit(Unit): # 클래스 내에 메소드에선 self 꼭 적기!
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed) ## 이렇게 상속받은거에 __init__활용 가능
        self.damage = damage
        print("{0} 유닛이 생성됐습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다, [공격력 {2}]".format(\
            self.name, location, self.damage)) # self. 이 붙은건 __init__에서 받을거야~

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} 현재 채력은 {1} 입니다".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} 유닛은 파괴됐습니다".format(self.name))

class Flyable : 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}, {1} 방향으로 날아갑니다 [속도 : {2}]"\
            .format(name, location, self.flying_speed))
    
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage, 0) # 지상 이동 0 
        Flyable.__init__(self, flying_speed)
    
    def move(self, location):
        print("[공중 유닛 이동]")
        self.fly(self.name, location)
# # 벌쳐 : 지상 유닛, 기동성이 좋다

# vulture = AttackUnit("벌쳐", 80, 20, 10)
# battlecruiser = FlyableAttackUnit("배틀크루저", 500, 25, 3)

# vulture.move("11시")
# # battlecruiser.fly(battlecruiser.name, "9시")
# battlecruiser.move("9시")
# # 항상 지상 / 공중유닛을 확인해야해.. 너무 귀찮지
# # 그래서 그냥 처리함


# 건물 =? super란!!!!!

# class BuildingUnit(Unit):
#     def __init__(self, name, hp, location):
#         pass # 아무것도 안 해도 넘어간다~~~~
# supply_dopot = BuildingUnit("서플라이디폿", 500, "7시")

# def game_start():
#     print("[알림] 새로운 게임을 시작합니다.,")
# def game_over():
#     pass

# game_start()
# game_over() # 매끄럽게 실행 가능 ~ 

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__( name, hp, 0)
        self.location = location
