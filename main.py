equ = input('Enter your Equation: \n').strip().split("=")

for i in range(100):
    x = i
    e = eval(equ[0])
    if e == int(equ[1]):
        print(x)
        break

