text = "P = 3.14!"

digits_count = 0
uppercase_count = 0
lowercase_count = 0
other_count = 0

for char in text:
    code = ord(char)
    if 48 <= code <= 57:
        digits_count += 1
    elif 65 <= code <= 90:
        uppercase_count += 1
    elif 97 <= code <= 122:
        lowercase_count += 1
    else:
        other_count += 1

print(f"Аналізований рядок: {text}")
print(f"Кількість цифр: {digits_count}")
print(f"Кількість великих латинських літер: {uppercase_count}")
print(f"Кількість малих латинських літер: {lowercase_count}")
print(f"Кількість інших символів: {other_count}")
