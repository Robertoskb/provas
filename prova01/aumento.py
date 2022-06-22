def aumentar(salario):
    if salario <= 1000:
        aumento = .2

    elif salario <= 1500:
        aumento = .15

    elif salario <= 2000:
        aumento = .1

    else:
        aumento = .05

    return salario + salario * aumento


atual = float(input())
print(f'{aumentar(atual):.2f}')
