from random import *

def game_start():
    print("[알림] : 새로운 게임을 시작합니다.")

def game_over():
    print("player 1 : gg")
    print("[player] 님이 게임에서 퇴장하셨습니다.")


class Unit: # 일반 유닛
    def __init__(self, name, hp, speed):
        self.name = name
        self.hp = hp
        self.speed = speed
        print("{0} 유닛이 생성됐습니다.".format(name))
        
    def move(self, location):
        #print("[지상 유닛 이동]")
        print("{0} : {1} 방향으로 이동합니다. [속도 : {2}]"\
            .format(self.name, location, self.speed))

    def damaged(self, damage):
        print("{0} : {1} 데미지를 입었습니다".format(self.name, damage))
        self.hp -= damage
        print("{0} 현재 채력은 {1} 입니다".format(self.name, self.hp))

        if self.hp <= 0:
            print("{0} 유닛은 파괴됐습니다".format(self.name))



class AttackUnit(Unit): # 클래스 내에 메소드에선 self 꼭 적기!
    def __init__(self, name, hp, damage, speed):
        Unit.__init__(self, name, hp, speed) ## 이렇게 상속받은거에 __init__활용 가능
        self.damage = damage
        # print("{0} 유닛이 생성됐습니다".format(self.name))
        print("체력 {0}, 공격력 {1}".format(self.hp, self.damage))
    
    def attack(self, location):
        print("{0} : {1} 방향으로 적군을 공격합니다, [공격력 {2}]".format(\
            self.name, location, self.damage)) # self. 이 붙은건 __init__에서 받을거야~

# 마린
class Marine(AttackUnit):
    def __init__(self):
        AttackUnit.__init__(self, "마린", 40, 5, 1)

    def stimpack(self):
        if self.hp > 10 :
            self.hp -= 10
            print("{0}이 스팀팩을 사용합니다.(HP 10 감소)".format(self.name))
        else:
            print("{0}이 체력이 부족하여 사용불가".format(self.name))

class Tank(AttackUnit): # 시즈모드, 업그레이드하면 모든 탱크에 설정가능
    seize_developed = False

    def __init__(self):
        AttackUnit.__init__(self, "시즈탱크", 150, 35, 1)
        self.seize_mode = False

    def set_seize_mode(self):
        if Tank.seize_developed == False:
            return
        # 시즈모드가 아닐 떄 -> 시즈 모드
        if self.seize_mode == False:
            print("{0} : 시즈 모드로 전환합니다".format(self.name))
            self.damage *= 2
            self.seize_mode = True
        # 시즈모드 일 때  -> 시즈 모드 해제
        else:
            print("{0} : 시즈 모드로 해제합니다".format(self.name))
            self.damage /= 2
            self.seize_mode = False
        



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
        #print("[공중 유닛 이동]")
        self.fly(self.name, location)

class wraith(FlyableAttackUnit):
    def __init__(self):
        FlyableAttackUnit.__init__(self, "레이스",80,5,20)
        self.clocked = False
    
    def clocking(self):
        if self.clocked == True:
            print("{0} : 클로킹 모드 해제".format(self.name))
            self.clocked = False
        else:
            print("{0} : 클로킹 모드 설정".format(self.name))
            self.clocked = False

    

class BuildingUnit(Unit):
    def __init__(self, name, hp, location):
        # Unit.__init__(self, name, hp, 0)
        super().__init__( name, hp, 0)
        self.location = location


## 실제 게임 진행

game_start()

m1 = Marine()
m2 = Marine()
m3 = Marine()

t1 = Tank()
t2 = Tank()

w1 = wraith()

# 유닛 일괄 관리

attack_units = []
attack_units.append(m1)
attack_units.append(m2)
attack_units.append(m3)
attack_units.append(t1)
attack_units.append(t2)
attack_units.append(w1)

# 전군 이동

for unit in attack_units:
    unit.move("1시")

# 탱크 시즈 모드 개발
Tank.seize_developed = True
print("[알림] : 탱크 시즈모드 개발 완료")

# 공격 모드 준비 (탱크 : 시즈모드, 레이스: 클로킹, 마린 : 스팀팩)

for unit in attack_units: # 경우의 수 나누기~ 
    if isinstance(unit, Marine):
        unit.stimpack()
    elif isinstance(unit, Tank):
        unit.set_seize_mode()
    else:
        unit.clocking()

for unit in attack_units:
    unit.attack("1시")


# 전군 피해 

for unit in attack_units:
    unit.damaged(randint(5, 21)) # 5~20 사이의 공격을 랜덤으로 받음

# 게임 종료
game_over()
