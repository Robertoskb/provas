P = int(input())
S = int(input())
E = int(input())

altura = 0
while True:
    nova_altura = altura + S
    print(f'{altura} {nova_altura if nova_altura < P else "saiu"}')
    altura = nova_altura - E

    if nova_altura >= P:
        break
