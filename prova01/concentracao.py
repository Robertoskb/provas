def gerar(a, b):
    ad = [iter(range(b, a-1, -1)), iter(range(a, b+1))]
    while True:
        value = ad.pop()
        try:
            yield next(value)

        except StopIteration:
            return

        ad.insert(0, value)


A = int(input())
B = int(input())

print(f'[{" ".join(map(str, gerar(A, B)))}]')
