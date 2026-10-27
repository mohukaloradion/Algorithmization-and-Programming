consumption = [4, 2, 7, 1, 9, 3, 5]
queries = [(1, 3), (0, 4), (2, 5)]

prefix_sums = [0] * (len(consumption) + 1)
for i in range(len(consumption)):
    prefix_sums[i + 1] = prefix_sums[i] + consumption[i]

print("Результати запитів енергоспоживання (з індексу по індекс):")
for start, end in queries:
    total_period_consumption = prefix_sums[end + 1] - prefix_sums[start]
    print(f"Період з {start} по {end}: {total_period_consumption} кВт·год")
