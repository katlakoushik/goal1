class Calculator:
    def Addition(self, a, b):
        return a + b
    def Subtraction(self, a, b):
        return a - b
    def Multiplication(self, a, b):
        return a * b
    def Division(self, a, b):
        if b == 0:
            print('Division by zero not possible')
        else:
            return a / b
obj=Calculator()

a=int(input('Enter a number: '))
b=int(input('Enter another number: '))
print("Addition  =",obj.Addition(a,b))
print("Subtraction =",obj.Subtraction(a,b))
print("Multiplication =",obj.Multiplication(a,b))
print("Division =",obj.Division(a,b))
