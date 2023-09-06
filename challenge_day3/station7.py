from sympy import symbols, sympify
def solution_station_7(observations):
    a, b, c, d, e = symbols('a b c d e')
    parsed_expression = sympify(observations)
    result = parsed_expression.subs({a: 3, b: -1, c: 4, d: 7, e: 0.5})
    return (round(result,1))