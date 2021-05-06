class LunchMenu:
    def get_restaurant_input(self):
        self.dict_list = []
        sel = int(input('1번은 식당명 메뉴 생성, 2번은 종료 : '))
        while True:
            if sel == 1:
                print("===== 식당명 메뉴 추가 중 =====")
                my_dict = {}  # empty dictionary
                rest = 'restuarant'
                val = input('식당명 입력 : ')
                my_dict[rest] = val

                menu = 'food'
                val = input('음식 입력 : ')
                my_dict[menu] = val

                price = 'price'
                val = input('가격 입력 : ')
                my_dict[price] = val
                self.dict_list.append(my_dict)
                con = int(input('1번은 식당명 메뉴 추가 계속, 2번은 종료 : '))
                if con == 2:
                    print("===== 추가 끝 =====")
                    break
            elif sel == 2:
                print("종료합니다.")
                break
            else:
                print("잘못 선택하셨습니다.")
                break
        return self.dict_list
    pass