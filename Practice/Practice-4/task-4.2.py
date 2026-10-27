number = 12

is_even = (number & 1) == 0
is_power_of_two = (number > 0) & ((number & (number - 1)) == 0)
lowest_set_bit = number & -number
bit_count = number.bit_count()

print(f"Аналізоване число: {number} ({bin(number)})")
print(f"Число є парним?: {is_even}")
print(f"Число є степенем двійки?: {is_power_of_two}")
print(f"Молодший встановлений біт (значення): {lowest_set_bit} ({bin(lowest_set_bit)})")
print(f"Кількість встановлених бітів: {bit_count}")
