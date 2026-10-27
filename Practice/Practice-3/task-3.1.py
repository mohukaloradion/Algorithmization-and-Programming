item1 = 0.1
item2 = 0.2
expected_total = 0.3

calculated_total = item1 + item2
epsilon = 1e-9

is_valid = abs(calculated_total - expected_total) < epsilon

print(f"Пряме порівняння (0.1 + 0.2 == 0.3): {calculated_total == expected_total}")
print(f"Валідація з допуском епсилон: {is_valid}")
print(f"Фактична сума: {calculated_total}")
