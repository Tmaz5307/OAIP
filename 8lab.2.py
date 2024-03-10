def stars():
    a = input().split()
    print(*list(map(lambda x: x.rjust(len(max(a, key=len)), "*"), a)), sep='\n')


stars()
