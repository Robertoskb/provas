a = int(input())
b = int(input())

if a > b:
    print('invalido')

else:
    print(sum((n for n in range(a, b+1) if not n % 2)))
