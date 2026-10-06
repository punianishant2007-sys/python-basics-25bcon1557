n = int(input("Enter a number: "))

for i in range(n + 1):
    if i * (i + 1) == n:
        print("Pronic Number")
        break
else:
    print("Not a Pronic Number")
