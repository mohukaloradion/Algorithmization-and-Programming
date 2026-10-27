arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

max_so_far = arr[0]
current_max = arr[0]

start = 0
end = 0
temp_start = 0

for i in range(1, len(arr)):
    if arr[i] > current_max + arr[i]:
        current_max = arr[i]
        temp_start = i
    else:
        current_max = current_max + arr[i]

    if current_max > max_so_far:
        max_so_far = current_max
        start = temp_start
        end = i

sub_array = arr[start:end + 1]

print(f"Максимальна сума підмасиву {sub_array}: {max_so_far}")
