num = [1, 2, 3, 6, 8, 10, 5, 45]

largest = num[0]
second = None

for i in num:
    if i > largest:
        second = largest
        largest = i
    elif i < largest and (second is None or i > second):
        second = i

print(largest)
print(second)