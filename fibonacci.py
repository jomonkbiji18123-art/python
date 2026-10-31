n = int(input("Enter the number of terms: "))

a = 0
b = 1
terms = []

for _ in range(n):
    terms.append(a)
    a, b = b, a + b

print(*terms)