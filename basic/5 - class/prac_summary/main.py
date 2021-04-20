# encoding: euc-kr
'''
일주일 점심식단 추천

- 식당명들: 교동짬뽕, Nobrand Burger, 나주곰탕, Salady, Subway
- 가격 : 7,000원, 4,500원, 8,000원, 3,000원, 3500원
- 랜덤으로 선택
- 2일 연속 똑같은거 x
- 일주일 가격 3만원 한도
- 5일

- 몇일 오는지 입력
- 주변 식당 database
- 가격 data
- 일주일 상한가격

'''
import LunchMenu as lm
import RandomSelect as rs
import pickle
import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # 일주일에 몇일 출근?
    days = int(input(f"일주일에 몇 일 출근? "))
    # 주변 식당
    lunch = lm.LunchMenu()
    menu_list = lunch.get_restaurant_input()
    diet = {'restaurant': 'nope', 'food': 'nope', 'price': 0}
    menu_list.append(diet)
    # print
    print(f"입력한 레스토랑 메뉴들\n{menu_list}")

    df = pd.DataFrame(menu_list)

    df.to_excel('daum_real_time_keyword.xlsx', index=False)
    # # 랜덤 선택
    # limit = int(input(f"일주일 점심 budget: "))
    # selec = rs.RandomSelect(menu_list, days, limit)
    # selec.random_number()
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
