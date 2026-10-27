elements = [10, 20, 30, 40, 50, 60]

print(f"Список до реверсу: {elements}")

left = 0
right = 0
for _ in elements:
    right += 1
right -= 1

while left < right:
    elements[left], elements[right] = elements[right], elements[left]
    left += 1
    right -= 1

print(f"Список після реверсу: {elements}")
