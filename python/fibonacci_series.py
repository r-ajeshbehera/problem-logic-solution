n = int(input("Enter the number of terms: "))
t1, t2 = 0, 1

print("Fibonacci Series:", end=" ")
for _ in range(n):
    print(t1, end=", ")
    t1, t2 = t2, t1 + t2
print()
