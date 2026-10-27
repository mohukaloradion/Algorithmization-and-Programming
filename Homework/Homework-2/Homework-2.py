number = int(input())

hundreds = number // 100
tens = (number // 10) % 10
units = number % 10

sum_of_squares = hundreds**2 + tens**2 + units**2

print(f"Сума квадратів цифр ({hundreds}^2 + {tens}^2 + {units}^2): {sum_of_squares}")
