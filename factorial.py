def factorial(num):
    print("Valor inicial ->",num)
    if num > 1:
        num = num * factorial(num -1)
    print("Valor inicial ->",num)
    return num

print(factorial(5))