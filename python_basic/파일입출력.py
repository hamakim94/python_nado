# score_file = open("score.txt",'w', encoding = "utf8") # utf8 써야 한글~

# print("수학 : 0", file = score_file)
# print("영어 : 50", file = score_file)
# score_file.close()

# score_file = open("score.txt", 'a', encoding = "utf8") # append : 뒤에 이어서 쓸래~
# score_file.write("과학 : 80")
# score_file.write("\n코딩 : 100")
# score_file.close()

#읽기
# score_file = open("score.txt", 'r', encoding='utf8')

# print(score_file.read()) # 다읽어라~

# print(score_file.readline(), end = "") # 줄별로 읽기, 커서는 다음 줄로 이동
# print(score_file.readline(), end = "")
# print(score_file.readline(), end = "")
# print(score_file.readline(), end = "")

#내가 모를떄~
# while True: 
#     line = score_file.readline()
#     if not line:
#         break
#     print(line, end = "")
# score_file.close()

# list 안에 넣어버리기

score_file = open("score.txt", 'r', encoding='utf8')
lines = score_file.readlines()
for line in lines:
    print(line, end = "")
score_file.close()