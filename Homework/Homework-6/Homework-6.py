text = "hello"
shift = 3

encrypted_text = ""

for char in text:
    base = ord('a')
    code = ord(char) - base
    new_code = (code + shift) % 26
    encrypted_text += chr(base + new_code)

print(f"Зашифрований текст: \"{encrypted_text}\"")
