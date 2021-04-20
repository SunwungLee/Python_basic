class FourCal:
    # 따로 선언 안해주어도 쓸 수 있다.
    # inp_x=0
    # inp_y=0
    def setdata(self, x, y):
        # FourCal.inp_x = x
        # FourCal.inp_y = y
        self.inp_x = x
        self.inp_y = y
    def add(self):
        # return FourCal.inp_x + FourCal.inp_y
        return self.inp_x + self.inp_y

    def sub(self):
        # return FourCal.inp_x - FourCal.inp_y
        return self.inp_x - self.inp_y

    def mul(self):
        # return FourCal.inp_x * FourCal.inp_y
        return self.inp_x * self.inp_y

    def div(self):
        # return FourCal.inp_x / FourCal.inp_y
        return self.inp_x / self.inp_y

if __name__ == '__main__':
    a = FourCal()
    b = FourCal()

    a.setdata(1,2)
    b.setdata(3,4)

    print(f"a input: x={a.inp_x}, y={a.inp_y}")
    print(f"b input: x={b.inp_x}, y={b.inp_y}")

    print(f"add method: {a.add()}")
    print(f"sub method: {a.sub()}")
    print(f"mul method: {a.mul()}")
    print(f"div method: {a.div()}")

