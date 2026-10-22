import sympy as sp

def run_sympy():
    x = sp.Symbol('x')
    expr = sp.diff(x**2 + 3*x, x)
    return f'SymPy Derivative of x^2 + 3x: {expr}'
