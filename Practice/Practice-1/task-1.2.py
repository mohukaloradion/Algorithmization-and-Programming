price = 350
discount_percentage = 10

discount_amount = price * (discount_percentage / 100)
final_price = price - discount_amount

print(f"Ціна: {price}")
print(f"Знижка {discount_percentage}%: {discount_amount}")
print(f"Зі знижкою: {final_price}")
