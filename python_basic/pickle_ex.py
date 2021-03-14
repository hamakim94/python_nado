# 파일 읽기 쉬움

# import pickle
# profile_file = open("profile.pickle", 'wb') # 피클을 쓰기 위해선 바이너리 타입 설정b
 # 인코딩 설정 따로 필요 없어


# profile = {"이름" : "박명수", "나이" : 30, "취미" : ["축구", "골프", "코딩"]}
# pickle.dump(profile, profile_file) # 프로필의 정보를 profile_file에 저장
# profile_file.close()

# 읽기

# profile_file = open("profile.pickle", 'rb')
# profile = pickle.load(profile_file) # file에 있는 정보를 profile_file에 불러온다
# print(profile)
# profile_file.close()

# with~?

import pickle

# with open("profile.pickle", 'rb') as profile_file:
#     print(pickle.load(profile_file))

# with open("study.txt", 'w', encoding = 'utf8') as study_file:
#     study_file.write("파이썬을 열심히 공부하고 있어용")

# with open("study.txt", 'r', encoding = 'utf8') as study_file:
#     print( study_file.readline() ) 


# Quiz

# with open("x주차.txt", 'w', encoding = "utf8") as week_report:
#     week_report.write("나는")
#     week_report.write("\n천재")


for i in range(1,51):
    with open("{0}주차.txt".format(i), 'w', encoding = "utf8") as week_report:
        week_report.write("- {} 주차 주간보고 - ".format(i))
        week_report.write("\n부서 :")
        week_report.write("\n이름 :")
        week_report.write("\n업무 요약 :")

# 

