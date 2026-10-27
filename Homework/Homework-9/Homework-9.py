def calculate_discount(price, discount_percent):
    if price < 0:
        raise ValueError("Ціна не може бути від'ємною")
    if not (0 <= discount_percent <= 100):
        raise ValueError("Відсоток знижки повинен бути в межах від 0 до 100")

    return price * (1.0 - discount_percent / 100.0)


assert calculate_discount(200.0, 15.0) == 170.0
assert calculate_discount(100.0, 0.0) == 100.0
assert calculate_discount(100.0, 100.0) == 0.0

try:
    calculate_discount(-10, 15)
    assert False
except ValueError:
    pass

try:
    calculate_discount(100, 105)
    assert False
except ValueError:
    pass

print(f"{calculate_discount(200.0, 15.0)} (автотести успішні)")
