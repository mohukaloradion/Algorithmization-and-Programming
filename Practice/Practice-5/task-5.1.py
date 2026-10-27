numbers = [14, -5, 23, 0, 8, -12, 7]

count = 0
total_sum = 0
min_val = numbers[0]
max_val = numbers[0]

for num in numbers:
    count += 1
    total_sum += num
    if num < min_val:
        min_val = num
    if num > max_val:
        max_val = num

average = total_sum / count if count > 0 else 0

print(f"Аналізований список: {numbers}")
print(f"Кількість елементів: {count}")
print(f"Сума елементів: {total_sum}")
print(f"Мінімальне значення: {min_val}")
print(f"Максимальне значення: {max_val}")
print(f"Середнє арифметичне: {average}")
