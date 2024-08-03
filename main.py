import sympy as sy
exp = input("your equation: \n").strip().split("=")
x = sy.symbols('x') #for assigning the symbol 
l = sy.sympify(exp[0])
r = sy.sympify(exp[1])
equ = sy.Eq(l,r)
solved = sy.solve(equ,x, dict=True)
print(solved)



"""
problems: 
    1. it doesn't take string (SOLVED)
    2. want to make the symbol changes 

"""