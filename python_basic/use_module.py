# import travel.thailand # 맨 뒤에 있는거 : 모듈이나 패키지만 가능, 클래스/함수 불가
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# import travel.thailand.ThailandPackage # ModuleNotFoundError: No module named 'travel.thailand.ThailandPackage'; 'travel.thailand' is not a package
# trip_to = travel.thailand.ThailandPackage()
# trip_to.detail()

# 대신 from import 구문에서는 클래스,함수도 임포트 가능
# from travel.thailand import ThailandPackage
# trip_to = ThailandPackage()
# # trip_to.detail()

# from travel import vietnam
# trip_to = vietnam.VietnamPackage()
# trip_to.detail()

# from random import *

# from travel import * # NameError: name 'vietnam' is not defined
# trip_to = vietnam.VietnamPackage() # travel 패키지에 있는거 다 가져올건데, 공개 범위를 설정 해줘야해
# trip_to.detail()
# 공개/비공개 따로 설정 가능 

# trip_to = thailand.ThailandPackage() # travel 패키지에 있는거 다 가져올건데, 공개 범위를 설정 해줘야해
# trip_to.detail() # __all__ = ["vietnam"] 만 공개해줘서 안댐

## 근데 만약 내가 위치를 확인하고싶어?
from travel import *
import inspect
import random

print(inspect.getfile(random))
print(inspect.getfile(thailand))