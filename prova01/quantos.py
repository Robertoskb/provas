pontos = [input() for _ in range(3)]
repetidas = pontos.count(max(pontos, key=lambda p: pontos.count(p)))

print(0 if repetidas == 1 else repetidas)
