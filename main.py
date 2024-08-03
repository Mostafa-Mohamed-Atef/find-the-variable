import sympy as sy
exp = input("your equation: \n").strip().split("=")
x = sy.symbols('x') #for assigning the symbol 
l = sy.sympify(exp[0])
r = sy.sympify(exp[1])
eqx = sy.Eq(l,r)
solved = sy.solve(eqx)
print(solved)