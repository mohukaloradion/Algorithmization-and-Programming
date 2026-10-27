numbers = [12, 45, 2, 89, 34, 6, 90, 23]

min_val = numbers[0]
max_val = numbers[0]

for num in numbers:
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

difference = max_val - min_val

print(f"Мінімум: {min_val}, Максимум: {max_val}, Різниця: {difference}")
