class House:
    # 매물 초기화

    def __init__(self, location, house_type, deal_type, price, completion_year):
        self.location = location
        self.house_type = house_type
        self.deal_type = deal_type
        self.price = price
        self.completion_year = completion_year

    # 매물 정보 표시

    def show_detail(self):
        # print("총 {}대의 매물이 있습니다".format(self.total_number))
        print(self.location, self.house_type, self.deal_type,\
             self.price, self.completion_year, sep = " ")

a = House("강남", "아파트", "매매", "10억", "2010년")
b = House("마포", "오피스텔", "전세", "5억", "2007년")
c = House("송파", "빌라", "월세", "500/50", "2000년")
house_list = [a,b,c]

print("총 {}대의 매물이 있습니다.".format(len(house_list)))
for house in house_list:
    house.show_detail()


