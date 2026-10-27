import math

a = 3.0
b = 4.0
expected_c = 5.0

c = math.sqrt(a**2 + b**2)
perimeter = a + b + c

epsilon = 1e-6
is_match = abs(c - expected_c) < epsilon

print(f"Гіпотенуза: {c}, Периметр: {perimeter}, Збігається: {is_match}")
