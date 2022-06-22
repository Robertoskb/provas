jogadores = {f'jog{i+1}': int(input()) for i in range(3)}

ganhador = max(jogadores, key=lambda j: list(jogadores.values()).count(jogadores[j]) == 1)

if not (sum(jogadores.values()) == 3 or sum(jogadores.values()) == 0):
    print(ganhador)

else:
    print('empate')
