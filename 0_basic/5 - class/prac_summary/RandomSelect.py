import random as rdm
import fractions
class RandomSelect():
    def __init__(self, list, days, limit):
        self.list = list
        self.days = days
        self.limit = limit

    def selection(self):
        tmp_dic = {}
        self.fianldiet = {}
        #tmp_dic = list[random_num]
        limitation = self.limit
        diet = list.get
        while True:
            random_num = rdm.randint(0, len(self.list) - 1) # 메뉴들 중 하나 뽑음.
            tmp_dic = list[random_num]
            tmp_price = tmp_dic.get('price')
            if (limitation - tmp_price) >= 0:
                self.finaldiet.append(tmp_dic)
                limitation -= tmp_price
            else: # budget 초과한다면, diet 값 출력
                self.finaldiet.append





    pass

if __name__ == "__main__":
    a = rdm.randint(0, 10)
    print(a)
    print(type(a))
    frac1 = fractions.Fraction(2, 3)
    print(frac1)

    # dictionary 하나
    # 난수 생성
    # 난수에 맞는거 list에서 뽑아와서 tmp저장
    # budget checking
    # 점심에 저장
    # budget 초과하면 diet로 채움
    # 전체 simul 다시 진행