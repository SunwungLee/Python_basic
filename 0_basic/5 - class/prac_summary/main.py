# encoding: euc-kr
'''
������ ���ɽĴ� ��õ

- �Ĵ���: ����«��, Nobrand Burger, ���ְ���, Salady, Subway
- ���� : 7,000��, 4,500��, 8,000��, 3,000��, 3500��
- �������� ����
- 2�� ���� �Ȱ����� x
- ������ ���� 3���� �ѵ�
- 5��

- ���� ������ �Է�
- �ֺ� �Ĵ� database
- ���� data
- ������ ���Ѱ���

'''
import LunchMenu as lm
import RandomSelect as rs
import pickle
import pandas as pd

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # �����Ͽ� ���� ���?
    days = int(input(f"�����Ͽ� �� �� ���? "))
    # �ֺ� �Ĵ�
    lunch = lm.LunchMenu()
    menu_list = lunch.get_restaurant_input()
    diet = {'restaurant': 'nope', 'food': 'nope', 'price': 0}
    menu_list.append(diet)
    # print
    print(f"�Է��� ������� �޴���\n{menu_list}")

    df = pd.DataFrame(menu_list)

    df.to_excel('daum_real_time_keyword.xlsx', index=False)
    # # ���� ����
    # limit = int(input(f"������ ���� budget: "))
    # selec = rs.RandomSelect(menu_list, days, limit)
    # selec.random_number()
    pass

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
