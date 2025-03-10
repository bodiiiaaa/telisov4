def multiply_digits_until_single(n):
    while n > 9:
        a = 1
        for digit in str(n):
            a *= int(digit)
        n = a
    return n

num = int(input("Введіть число: "))

result = multiply_digits_until_single(num)

print("Результат:", result)
