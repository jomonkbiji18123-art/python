num = [int(x.strip()) for x in input("Enter numbers separated by commas: ").split(",")]

for i in range(len(num)):
    for j in range(i + 1, len(num)):
        if num[i] > num[j]:
            num[i], num[j] = num[j], num[i]

print(num)