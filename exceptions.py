# 예외 처리
try:
    print("나누기 전용 계산기입니다.")
    nums = []
    nums.append( int(input("첫 번째 숫자를 입력하세요 : ")) )
    nums.append( int(input("두 번째 숫자를 입력하세요 : ")))
    nums.append(int(nums[0] / nums[1]))
    #  print("{0} / {1} = {2}".format(nums[0],nums[1], nums[2]))
# 6, '삼'이라고 넣으면 Value Error가 뜬다
except ValueError: # 문제가 발생 하면 , 발생하는 오류에 대한 명령어가 실행돼6
    print("에러! 잘못된 값을 입력하였습니다")
except ZeroDivisionError as err:
    print(err) #
except Exception as err:
    print("알 수 없는 오류가 발생하였습니다") # except하고 특정 Error를 안 하면 다 바뀜..
    print(err)
# 0으로 나누면 ZeroDivisionErro 나옴


try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 =  int(input("첫 번째 숫자를 입력하세요 : ")) 
    num2 =  int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise ValueError
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except ValueError:
print("잘못된 값을 입력했습니다")



사용자 정의 예외처리 -> 직접 error를 정의해서 만들기

class BigNumberError(Exception): # Exception class 상속 
    def __init__(self, msg):
        self.msg = msg
    
    def __str__(self):
        return self.msg
try:
    print("한 자리 숫자 나누기 전용 계산기입니다.")
    num1 =  int(input("첫 번째 숫자를 입력하세요 : ")) 
    num2 =  int(input("두 번째 숫자를 입력하세요 : "))
    if num1 >= 10 or num2 >= 10:
        raise BigNumberError( "입력 값: {0}, {1}".format(num1,num2))
    print("{0} / {1} = {2}".format(num1, num2, int(num1 / num2)))
except BigNumberError as err:
    print("에러가 발생하였습니다. 한 자리 숫자만 입력하세용~")
    print(err)

finally:
    print("계산기를 이용해주셔서 매우 감사룽~")


# finally : 예외 처리 중에서 정상적으로 수행이 되건 오류가 되건 무적권 실행되는 구문

