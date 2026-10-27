import math

a = 10000.0
b = 10000.0
c = 0.0001

p = (a + b + c) / 2
radicand = p * (p - a) * (p - b) * (p - c)

safe_radicand = max(0.0, radicand)
area = math.sqrt(safe_radicand)

print(f"Початковий підкореневий вираз: {radicand}")
print(f"Безпечний підкореневий вираз: {safe_radicand}")
print(f"Площа трикутника: {area}")
