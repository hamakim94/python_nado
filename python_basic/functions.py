
# 가변인자

# def profile(name, age, lang1, lang2, lang3, lang4, lang5):
#     print( "이름 : {0}\t나이 : {1}\t".format(name,age), end = " ")
#     print(lang1, lang2, lang3, lang4, lang5)

# profile("유재석", 20 , "Python", "Java", "C", "C++", "C#")
# profile("유재석", 25 , "Kotlin", "Swift", "", "", "") #빈 값 넣기 너무 귀찮네..?, 
 # 여러개인게 어떻게?

# def profile(name, age, *language):
#     print( "이름 : {0}\t나이 : {1}\t".format(name,age), end = " ")
#     for lang in language: # 가변인자는 이렇게 써야해
#         print(lang, end = " ")
#     print() # for 줄바꿈

# profile("유재석", 20 , "Python", "Java", "C", "C++", "C#", "JavaScript")
# profile("유재석", 25 , "Kotlin", "Swift") #빈 값 넣기 너무 귀찮네..?, 

# 지역변수(함수내) 와 전역변수 : 프로그램 내 어디서든

gun = 10

def checkpoint(soldiers):
    # gun = 20
    global gun # 전역 공간에 있는 gun 사용 
    gun = gun - soldiers # 이건 지역변수야..  local variable 'gun' referenced before assignment

    print("[함수 내] 남은 총 : {0}".format(gun))

# 이걸 쓰면 전역변수 처럼 쓸 수 있다~
# def checkpoint_ret(gun, soldiers):
#     gun = gun - soldiers
#     print("[함수 내] 남은 총 : {0}".format(gun))
#     return gun # **


# print("전체 총 : {0}".format(gun)) # 10이나옴
# gun = checkpoint_ret(gun, 2)                     # 18이나옴
# print("남은 총 : {0}".format(gun))# 10이나옴


# Quiz

# 얻은점 : 함수 내부에서 지역변수는 새로 만들 수 있음, 따로 설정 안 해도 돼
# 그런데 아마 하는게 좋다.. 가독성떄문에..

def std_weight(height, gender):
    if gender == "남자":
        weight = (height/100) * (height/100) * 22
        print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, round(weight,2)))
        return weight
    elif gender == "여자" :
         weight = (height/100) * (height/100) * 21
         print("키 {0}cm {1}의 표준 체중은 {2}kg 입니다.".format(height, gender, round(weight,2)))
    else:
         print("성별을 제대로 입력해주세요")

std_weight(175, "여자") 
# syntax error 뜬다,, -> 괄호 보자

# 답은 훨씬 더 간단해
# 문제에선 표준 체중을 우선 계산하고,
# 출력을 해라

def std_wei(height, gender): # 신장은 M단위로 받는다면
    if gender == "남자":
        weight = height * height * 22
        return weight
    else:
        weight = height * height * 21
        return weight
height = 175
gender = "남자"
weight = std_wei(height / 100, gender)
print(weight)
print("키 {0}cm {1}의 표준 체중은 {2}입니다.".format(height, gender, round(weight,2)))


    
        