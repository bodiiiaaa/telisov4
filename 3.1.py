a= float(input("Введіть перше число :"))
b= input("Введіть дію (+, -, *, /): ")
c= float(input("Введіть друге число:"))

if b == '+':
    print(a+c)
elif b == '-':
    print(a-c)
elif b == '*':
    print(a*c)
elif b == '/':
    if c == 0:
        print('Ділення на нуль неможливе')

else:
    print('Невірна дія ')





