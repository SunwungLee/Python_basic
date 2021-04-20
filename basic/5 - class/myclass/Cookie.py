'''
class 만들기 예제
'''
class Cookie:
    x = 123 # 변수선언 & 값 할당
    y = 1.2
    def __init__(self, name):
        Cookie.name = name
        Cookie.yy = 2

    def add(self, a, b): # class 내의 method 선언
        return a+b
    def mul(self):
        return self.x*self.y


xy = Cookie() # 객체 생성
print(xy.add(1, 2))
print(xy.x)
print(xy.mul())

x = 2,
y = 3
# xy1 = Cookie(x, y) # 객체 생성, parameter로 매개변수 지정해서 객체로 만듦.

