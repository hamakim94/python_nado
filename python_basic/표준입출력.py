# import sys
# print("Python", "Java", "JavaScript", file = sys.stdout)#표준출력
# print("Python", "Java", "JavaScript", file = sys.stderr)#표준에러 이럴떈 따로 처리해줄 수 있음

# 정렬
# scores = { "수학" : 0 , "영어" : 50, "코딩" : 100}
# for subject, score in scores.items():
#     # print(subject,score)
#     print(subject.ljust(5),str(score).rjust(4), sep = ",") # 문자열만 ljust, rjust 가능

# 은행 대기순번표
# 001,002,
# for num in range(1,21):
#     print("대기번호 : {}".format(str(num).zfill(3))) # str.zfill(i) : i공간, 없으면 0 채워

# 표준입출력 -> 항상 문자

# answer = input("아무 값이나 입력하세요 : ")
# print(type(answer10))
# print("입력하신 값은 {0}입니다.".format(answer))

# 빈 자리는 빈공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간 확보
print("{0: >10}".format(500))
# 양수일 떄는 +로 표시, 음수일 땐 -로 표시
print("{0: >+10}".format(500))
print("{0: >+10}".format(-500)) # 저기 +때문에 +,- 함

# 왼쪽 정렬하고, 빈칸으로 _로 채움
print("{0:_<+10}".format(500))
# 3자리마다 콤마를 찍어주기
print("{0:,}".format(10000000000))
# 3자리마다 콤마를 찍어주기, +- 
print("{0:+,}".format(10000000000)) # comma 앞에다가 + 를 넣어줘야함
print("{0:+,}".format(-10000000000)) 

# 3자리마다 , 부호 붙여, 자릿수 30개, +/- 붙여, 빈자리 ^
print("{0:^<+30,}".format(1000000000))

#소수점
print("{0:f}".format(5/3))
#소수점 특정 자리수만 표현?
print("{0:.2f}".format(5/3)) # 2째자리까지, 셋 쨰 자리에서 반올림