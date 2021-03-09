# 몰랐던거
# 1.문자열 method에서, find와 index의 차이
# find, index 모두 문자열 내에서 특정 글자를 찾아줌
# 차이점 : find는 만약 답이 없으면 -1을 반환, index는 오류다
# python = "Python is easy"
# index = python.index("n") 
# print(python.index("n")) # 5 가 나오고, 더 나아가
# index = python.index("n", index + 1) 이렇게 하면 두 번쨰 n을 찾을 수 있음
# print(index)
# python.index("Java") -> 오류
# python.find("Java") -> -1

# # 방법 1
# print("나는 %d살 입니다" % 20) # %d는 정수만
# print("나는 %s를 좋아해요" % "python") # %s는 문자열~, 근데 숫자도 되긴 함
# print("Apple이라는 숫자는 %c로 시작해요." % "A")

# print("나는 %s색과 %s색을 좋아해요." %("파란", "빨간"))

# # 방법 2 
# print("나는 {}살 입니다".format(20))
# print("나는 {}색과 {}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {0}색과 {1}색을 좋아해요.".format("파란", "빨간"))
# print("나는 {1}색과 {0}색을 좋아해요.".format("파란", "빨간"))

# # 방법 3
# print("나는 {age}살이며, {color}색을 좋아해요".format(age = 20, color = "빨간"))
# print("나는 {age}살이며, {color}색을 좋아해요".format(color = "빨간", age = 20)

# # 방법4 : 문자열 앞에 f를 넣고, {}안에 변수를 넣으면 돼 
# age = 20
# color = "빨간"
# print(f"나는 {age}살이며, {color}색을 좋아해요")

# 탈출 문자

# \n : 줄바꿈
# print("백문이 불여일견 \n백견이 불여일타")

# \', \" : 문장 내에서 따옴표
# 저는 "나도코딩"입니다.
# print("저는 "나도코딩" 입니다.") # 따옴표 2개면 안대 
# print('저는 "나도코딩" 입니다.') # 따옴표 2개면 안대 
# print("저는 \"나도코딩\" 입니다.")

# print("C:\Users\User\Desktop\youtube-python>") # 역슬러쉬때문에 2개 넣으면 대
# print("C:\\Users\\User\\Desktop\\youtube-python>") # 역슬러쉬때문에 2개 넣으면 대

# \r : 커서를 맨 앞으로 이동
#print("Red Apple\rPine")

# \b : 백스페이스 (한 글자 삭제)
#print("Redd\bApple")

# \t : 탭 (4칸, 8칸 이동)
# print("Red\tApple")

# domain = "http://naver.com"
# for_id = domain[7:]
# # print(for_id)
# index = for_id.index('.')
# print(index)
# for_id = for_id[:index]
# print(for_id)

# for_id = for_id[:3] + str(len(for_id)) + str(for_id.count("e")) + "!"
# print(for_id)

# 답
url = "http://google.com"
my_str = url.replace("http://", "")
print(my_str)
my_str = my_str[:my_str.index(".")] 
print(my_str)

password = my_str[:3] + str(len(my_str)) + str(my_str.count("e")) + "!"
print("{}의 비밀번호는 {}입니다".format(url, password))
