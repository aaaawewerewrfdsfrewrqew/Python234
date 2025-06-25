num1 = int(input("введіть перше число: "))
num2 = int(input("введіть друге число: "))

sum_even = 0
sum_odd = 0
sum_divisible_by_9 = 0
a = 0
b = 0
c = 0

for i in range(num1, num2 + 1):
    if i % 2 == 0:
        sum_even += i
        a += 1
    elif i % 2 != 0:
        sum_odd += i
        b += 1
    if i % 9 == 0:
        sum_divisible_by_9 += i
        c += 1
        
print(f"середнє арифметичне парних чисел: {sum_even / a}")
print(f"середнє арифметичне непарних чисел: {sum_odd / b}")
print(f"середнє арифметичне чисел, кратних 9: {sum_divisible_by_9 / c}")

#2

dov = int(input("введіть довжину: "))
symbol = input("введіть символ: ")

for i in range(dov):
    print(symbol)

while True:
    num = int(input("Введіть число: "))
    if num > 0:
        print("number is positive")
    elif num < 0:
        print("numbwr is negative")
    else:
        print("mumber is equal to zero")
    
    if num == 7:
        print("good bye!")
        break

numbers = []

while 1:
    num = int(input("введіть число: "))
    if num == 7:
        print("Good bye!")
        break
    numbers.append(num)

if len(numbers) > 0:
    print("Сума:", sum(numbers))
    print("Максимум:", max(numbers))
    print("мінімум:", min(numbers))
else:
    print("жодного числа не введено.")
    
while 1:
    N = int(input("введіть ціле число N: "))
    
    if N <= 1:
        print("число має бути більшим за 1")
        break

    i = 2
    while i * i <= N:
        if N % i == 0:
            print("число", N, "не є простим.")
            break
        i = i + 1
    else:
        print("число", N, "є простим.")
        
N = int(input("введіть ціле число N: "))
a = 0
b = 1

if N == 0:
    print("число", N, "належить послідовності Фібоначчі")
else:
    while b < N:
        c = a + b
        a = b
        b = c

    if b == N:
        print("число", N, "належить послідовності Фібоначчі")
    else:
        print("число", N, "не належить послідовності Фібоначчі")
