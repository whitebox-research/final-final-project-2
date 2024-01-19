class Calc:
    def __init__(self, ex):
        self.ex = ex.replace(' ', '')
        self.i = 0

    def pse(self):
        try:
            return self.n()
        except Exception as e:
            return f"invalid: {e}"

    def n(self):
        sgn = False

        if self.ex[self.i] == '-':
            sgn = True
            self.i += 1
            
        if self.ex[self.i] == '(':
            self.i += 1
            out = None # TODO
            self.i += 1
            return -out if sgn else out
        
        i_0 = self.i
        while self.i < len(self.ex) and self.ex[self.i].isdigit():
            self.i += 1

        n = float(self.ex[i_0:self.i])
        return -n if sgn else n


if __name__ == '__main__':
    while True:
        try:
            eq = input("> ")
            calc = Calc(eq)
            out = calc.pse()
            print(out)
        except KeyboardInterrupt:
            exit()