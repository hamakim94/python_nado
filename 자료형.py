# 리스트
# pop() -> 마지막 제거
# .count() => 개수 세기
# .sort() 오름차순, .reverse(뒤집기)

# 딕셔너리   .get도 있어.. 
# cabinet = {3 : "유재석" , 100 : "김태호"}
# print(cabinet.get(5)) # get은 계속 지정 가능하지만, []는 없으면 오류뜬다
# print(cabinet.get(5, "사용 가능")) # 값이 없으면 사용가능이라는 값을 준다 ~ 

# # 간 손님
# del cabinet2["A-3"] # key를 삭제하는거야

# # 목욕탕 폐점
# cabinet2.clear()



# 튜플 -> 리스트보다 빨라, 그냥 지정 가능~
# 집합(set), 순서 x
# my_set = {1,2,3,3,3}
# print(my_set)

# java = {"유재석", "김태호", "양세형"}  # 이렇게 하면 set이다
# python = set(["유재석","박명수"])

# print(java & python) # 교집합
# print(java.intersection(python))

# print(java | python) # 합집합
# print(java.union(python))

# print(java - python) # 차집합, 자바만 할 수 있는 사람~
# print(java.difference(python))

# # python 할 줄 아는 사람 늘어남
# python.add("김태호 ")
# print(python)

# from random import *
# number = list(range(1,21,1))
# print(number)
# shuffle(number)
# print(number)

# print(" -- 당첨자 발표 -- \n치킨 당첨자 : {0} \n커피 당첨자 : {1}\n -- 축하합니다 -- ".format(number[0], number[1:4]))

# 답

from random import *
users = range(1,21)
users = list(users)

print(users)
shuffle(users)
print(users)

winners = sample(users, 4)
print(" -- 당첨자 발표 -- ")
print("치킨 당첨자 : {}".format(winners[0]))
print("커피 당첨자 : {}".format(winners[1:]))
print(" -- 축하합니다 --")