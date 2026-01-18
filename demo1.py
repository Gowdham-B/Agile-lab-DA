a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))
d= int(input("Enter fourth number: "))

if a >= b and a >= c and a >= d:
    print("Biggest number is:", a)
elif b >= a and b >= c and b >= d:
    print("Biggest number is:", b)
elif d >= a and d >= b and d >= c:
    print("Biggest number is:", d)
else:
    print("Biggest number is:", c)
