number = 13

mask = 1 << 3
is_bit_set = (number & mask) != 0

multiplied = number << 3

print(f"3-й біт увімкнений: {is_bit_set}, Число * 8: {multiplied}")
