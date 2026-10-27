text = "rar"
length = len(text)
is_palindrome = True

length = 0
for _ in text:
    length += 1

is_palindrome = True
left = 0
right = length - 1

while left < right:
    char_l = text[left]
    char_r = text[right]

    code_l = ord(char_l)
    code_r = ord(char_r)

    if 65 <= code_l <= 90:
        code_l += 32
    if 65 <= code_r <= 90:
        code_r += 32

    if code_l != code_r:
        is_palindrome = False
        break

    left += 1
    right -= 1

print(f"Рядок: {text}")
print(f"Чи є рядок паліндромом?: {is_palindrome}")
