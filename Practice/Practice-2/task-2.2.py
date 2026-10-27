number = 321

digit3 = number // 100
digit2 = (number // 10) % 10
digit1 = number % 10

reversed_number = digit1 * 100 + digit2 * 10 + digit3

print(reversed_number)
