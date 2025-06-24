
num1 = int(input("введіть перше число: "))
num2 = int(input("введіть друге число: "))

for i in range(num1, num2 + 1):
    if i % 7 == 0:
        print(i, end=" ")
print("\n числа, кратні 7, вказані вище.")
#2

num11 = int(input("введіть перше число: "))
num22 = int(input("введіть друге число: "))
kst = 0

for i in range(num11, num22 + 1):
    print(i, end=' ')
for i in range(num22, num11-1, -1):
    print(i, end=' ')
for i in range(num11, num22 + 1):
    if i % 7 == 0:
        print(i, end=' ')
for i in range(num11, num22 + 1):
    if i % 5:
        kst += 1
print(f"\nКількість чисел, кратних 5: {kst}")

#3

num111 = int(input("введіть перше число: "))
num222 = int(input("введіть друге число: "))

for i in range(num111, num222 + 1):
    if i % 3 == 0:
        print("fizz")
    elif i % 5 == 0:
        print("buzz")
    elif i % 3 == 0 and i % 5 == 0:
        print("fizz buzz")
    else:
        print(i)
#4

num1111 = int(input("введіть перше число: "))
num2222 = int(input("введіть друге число: "))
num3333 = int(input("введіть третє число: "))

dia = str(input("введіть порядок (+ або -): "))

if dia == "+":
    for i in (range(num1111, num2222 + 1, num3333)):
        print(i + num3333, end=' ')
    print("\nЧисла в порядку зростання з кроком", num3333)
elif dia == "-":
    for i in (range(num2222, num1111 - 1, -num3333)):
        print(i - num3333, end=' ')
    print("\nЧисла в порядку спадання з кроком", num3333)
    
#5

num11111 = int(input("введіть перше число: "))
num22222 = int(input("введіть друге число: "))
dob = 1
if num11111 < num22222:
    for i in range(num11111, num22222 + 1):
        if i % 4 == 0 and i % 6 != 0:
            dob *= i
            
elif num11111 > num22222:
    for i in range(num22222, num11111 + 1):
        if i % 4 == 0 and i % 6 != 0:
            dob *= i

print(f"Добуток чисел, кратних 4, але не кратних 6: {dob}")

#6

a = int(input("введіть число: "))
n = int(input("введіть ступінь числа: "))

b = a

for i in range(1, n + 1):
    b *= a
    
print(f"{a} в ступені {n} дорівнює {b}")
    
    



        

        