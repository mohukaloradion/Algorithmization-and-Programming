n = 10

if n <= 0:
    result = 0
elif n == 1:
    result = 1
else:
    a, b = 0, 1
    count = 2
    while count <= n:
        a, b = b, a + b
        count += 1
    result = b

print(f"{n} число Фібоначчі: {result}")
