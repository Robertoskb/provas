def aumentar(a, b):
    for i in range(a, b+1):
        yield i


def diminuir(a, b):
    for i in range(b, a-1, -1):
        yield i


def gerar(a, b):
    aum = aumentar(a, b)
    dim = diminuir(a, b)

    ad = [dim, aum]
    for i in range(b*2+1):
        try:
            value = ad.pop()
            yield next(value)

        except StopIteration:
            return

        ad.insert(0, value)


A = int(input())
B = int(input())

print(f'[{", ".join(map(str, gerar(A, B)))}]')
