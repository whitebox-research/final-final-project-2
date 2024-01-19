class Calc:
def __init__(self, ex):
    self.ex = ex.replace(' ', '')
    self.i = 0

def pse(self):
    try:
        return self.mul()
    except Exception as e:
        return f"invalid: {e}"

def mul(self):
    out = self.add()
    while self.i < len(self.ex):
        if self.ex[self.i] == '*':
            self.i += 1
            out *= self.add()
        elif self.ex[self.i] == '/':
            self.i += 1
            div = self.add()
            if div == 0:
                raise ZeroDivisionError
            out /= div
        else:
            break
    return out

def add(self):
    out = self.exp()
    while self.i < len(self.ex):
        if self.ex[self.i] == '+':
            self.i += 1
            out += self.exp()
        elif self.ex[self.i] == '-':
            self.i += 1
            out -= self.exp()
        else:
            break
    return out

def exp(self):
    out = self.n()
    while self.i < len(self.ex) and self.ex[self.i] == '^':
        self.i += 1
        out **= self.n()
    return out

def n(self):
    sgn = False

    if self.ex[self.i] == '-':
        sgn = True
        self.i += 1
        
    if self.ex[self.i] == '(':
        self.i += 1
        out = self.mul()
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
        # Ctrl-C to exit
        exit()