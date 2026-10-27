n = 30
prime_sum = 0
primes_list = []

for num in range(2, n + 1):
    is_prime = True
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        prime_sum += num
        primes_list.append(str(num))

primes_string = "+".join(primes_list)
print(f"Сума простих чисел від 2 до {n} ({primes_string}): {prime_sum}")
