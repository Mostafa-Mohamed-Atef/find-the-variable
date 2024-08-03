import sympy as sy
l, r = input("your equation: \n").strip().split("=")
eqx = sy.Eq(sy.sympify(l),sy.sympify(r))
solved = sy.solve(eqx)
print(solved)