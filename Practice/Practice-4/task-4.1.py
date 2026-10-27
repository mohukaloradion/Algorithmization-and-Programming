READ = 0b0001
WRITE = 0b0010
EXECUTE = 0b0100
ADMIN = 0b1000

user_permissions = READ | WRITE

has_read = (user_permissions & READ) != 0
has_execute = (user_permissions & EXECUTE) != 0

user_permissions = user_permissions | EXECUTE
has_execute_after_add = (user_permissions & EXECUTE) != 0

user_permissions = user_permissions & ~WRITE
has_write_after_remove = (user_permissions & WRITE) != 0

print(f"Початкові права (маска): {bin(READ | WRITE)}")
print(f"Має право на читання?: {has_read}")
print(f"Має право на виконання?: {has_execute}")
print(f"Має право на виконання після додавання?: {has_execute_after_add}")
print(f"Має право на запис після видалення?: {has_write_after_remove}")
