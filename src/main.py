class Calculator:
    def __init__(self, equation):
        self.equation = equation.replace(' ', '')
        self.index = 0

    def parse(self):
        try:
            return self.multiply()
        except Exception as e:
            return f"Error: {e}"

    def multiply(self):
        result = self.add()
        while self.index < len(self.equation):
            if self.equation[self.index] == '*':
                self.index += 1
                result *= self.add()
            elif self.equation[self.index] == '/':
                self.index += 1
                divisor = self.add()
                if divisor == 0:
                    raise ZeroDivisionError("Division by zero")
                result /= divisor
            else:
                break
        return result

    def add(self):
        result = self.exponentiate()
        while self.index < len(self.equation):
            if self.equation[self.index] == '+':
                self.index += 1
                result += self.exponentiate()
            elif self.equation[self.index] == '-':
                self.index += 1
                result -= self.exponentiate()
            else:
                break
        return result

    def exponentiate(self):
        result = self.numeric()
        while self.index < len(self.equation) and self.equation[self.index] == '^':
            self.index += 1
            result **= self.numeric()
        return result

    def numeric(self):
        is_negative = False

        if self.equation[self.index] == '-':
            is_negative = True
            self.index += 1

        if self.equation[self.index] == '(':
            self.index += 1
            result = self.multiply()
            self.index += 1
            return -result if is_negative else result

        start_index = self.index
        while self.index < len(self.equation) and self.equation[self.index].isdigit():
            self.index += 1

        number = float(self.equation[start_index:self.index])
        return -number if is_negative else number


if __name__ == '__main__':
    while True:
        try:
            equation = input("> ")
            calculator = Calculator(equation)
            result = calculator.parse()
            print(result)
        except KeyboardInterrupt:
            exit()
        except Exception as e:
            print(f"Error: {e}")
