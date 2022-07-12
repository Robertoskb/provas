P = int(input())
S = int(input())
E = int(input())

altura = 0
while altura + E < P:
    nova_altura = altura + S
    print(f'{altura} {nova_altura if nova_altura < P else "saiu"}')
    altura = nova_altura - E
