# class Unit:
#     def __init__(self,name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성됐습니다".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))

# # marine1 = Unit("마린", 50, 5 )
# # marine2 = Unit("마린2", 50, 5 )
# # tank1 = Unit("탱크", 150, 35 )
# # tank2 = Unit("탱크2", 150, 35 )

# # 클래스로부터 만들어 지는 것을 객체,  => 마린1, 마린2는 유닛 클래스의 인스턴스~
# # __init__ 은 생성자, 

# # marine = Unit("marine") # 오류

# # 멤버 변수 : 클래스 내에서 정의된 변수, 이걸 가지고 초기화 / 사용 가능

# # 레이스 : 공중 유닛, 비행기, 클로킹 ( 상대방에게 시야가 보이지 않는다 )

# wraith1 = Unit("레이스", 80 , 5)

# # 그렇다면 클래스 외부에서 멤버 변수를? -> .으로 접근 가능
# print("{0} 유닛, 공격력 {1}".format(wraith1.name, wraith1.damage))

# ## 마인드 컨트롤!

# wraith2 = Unit("빼앗은 레이스", 80, 5)
# wraith2.clocking = True # 외부에서 객체에 변수를 만들어서 사용 가능

# if wraith2.clocking == True: # 레이스 1에는 없네~
#     print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))

# if wraith1.clocking == True:
#     print("{0} 는 현재 클로킹 상태입니다".format(wraith2.name))

## method 





# 

# class AttackUnit: # 클래스 내에 메소드에선 self 꼭 적기!
#     def __init__(self,name,hp,damage):
#         self.name = name
#         self.hp = hp
#         self.damage = damage
#         print("{0} 유닛이 생성됐습니다".format(self.name))
#         print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
#     def attack(self, location):
#         print("{0} : {1} 방향으로 적군을 공격합니다, [공격력 {2}]".format(\
#             self.name, location, self.damage)) # self. 이 붙은건 __init__에서 받을거야~

#     def damaged(self, damage):
#         print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
#         self.hp -= damage
#         print("{0} 현재 채력은 {1} 입니다".format(self.name, self.hp))

#         if self.hp <= 0:
#             print("{0} 유닛은 파괴됐습니다".format(self.name))



# 상속 

# 공격력이 없는 경우는 어떻게? 

class Unit: # 일반 유닛
    def __init__(self,name,hp):
        self.name = name
        self.hp = hp


class AttackUnit(Unit): # 클래스 내에 메소드에선 self 꼭 적기!
    def __init__(self, name, hp, damage):
        Unit.__init__(self, name, hp) ## 이렇게 상속받은거에 __init__활용 가능
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

# firebat1 = AttackUnit("파이어뱃", 50, 16)
# firebat1.attack("5시")

# firebat1.damaged(25)
# firebat1.damaged(25)

## 다중상속.. 

# 드랍쉽 : 수송기.. 공중 유닛같은경운 어떻게 할래? 심지어 레이스도 ! 

class Flyable : 
    def __init__(self, flying_speed):
        self.flying_speed = flying_speed

    def fly(self, name, location):
        print("{0}, {1} 방향으로 날아갑니다 [속도 : {2}]"\
            .format(name, location, self.flying_speed))
    
# 공중 공격 유닛
class FlyableAttackUnit(AttackUnit, Flyable):
    def __init__(self, name, hp, damage, flying_speed):
        AttackUnit.__init__(self, name, hp, damage)
        Flyable.__init__(self, flying_speed)

# 발키리 : 공중 공격 유닛 한 번에 14발 미사일
valkyrie = FlyableAttackUnit("발키리", 200 , 6, 5 )
valkyrie.fly( valkyrie.name, "3시")



