prices = [100, 105, 102, 110, 108, 115, 120, 118]
window_size = 3

max_profit = 0

for i in range(len(prices) - window_size + 1):
    current_min = prices[i]
    current_max = prices[i]
    for j in range(i, i + window_size):
        if prices[j] < current_min:
            current_min = prices[j]
        if prices[j] > current_max:
            current_max = prices[j]

    profit = current_max - current_min
    if profit > max_profit:
        max_profit = profit

print(f"Максимальне коливання ціни у вікні розміром {window_size}: {max_profit}")
