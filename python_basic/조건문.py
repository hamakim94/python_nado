# input : 문자열로 받음

# 출석번호대로 이름을 부를거야, 근데 2, 5번 결석
# absent = [2,5]
# no_book = [7] # 책을 잊음

# for student in range(1,10):
#     if student in absent:
#         continue # 이건 그냥 실행을 안해 ~~, 대신 다시 위로 올라감, 아래 문장 실행 X
#     elif student in no_book:
#         print("오늘 수업 여기까지, {0}은 교무실로 따라와".format(student))
#         break # 그냥 아에 반복문을 탈출해버린다~
#     print("{0}, 책을 읽어봐".format(student))

# from random import *
# time = 0
# passenger_time = {}
# for passengers in range(1,51):
#     time = randint(5,50)
#     passenger_time[passengers] = time

# number = 0

# for pass_num, times in passenger_time.items():
#     if 5 <= times <= 15 :
#         number += 1
#         print("[O] {0}번째 손님 (소요시간 : {1}분)".format(pass_num, times))
#     else:
#         print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(pass_num, times))

# print("총 탑승 승객 : {0}분".format(number))
## 나는 굳이 dict에 넣어서 함,, 더 빠르게 하려면 .. 필요없는게 많았다.
# 답

from random import *
cnt = 0
for i in range(1,51): # 승객 : 1ㅡ50
    time = randrange(5,51) # 5,50사이에 뽑음
    if 5 <= time <= 15:
        print("[O] {0}번째 손님 (소요시간 : {1}분)".format(i, time))
        cnt += 1
    else:
        print("[ ] {0}번째 손님 (소요시간 : {1}분)".format(i, time))

print("총 탑승 승객 : {0}분".format(cnt))







