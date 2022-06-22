n = int(input())

points = '.' * len(str(n))

for i in range(1, n+1):
    print((points * (n-i) + (str(n) + points) * i + points * (n-i))[:-len(str(n))])
