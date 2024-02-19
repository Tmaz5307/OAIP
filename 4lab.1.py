def horse2(cell):
    a = 'abcdefgh'
    b = [(-2, 1), (-1, 2), (1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1)]
    x = a.find(cell[0]) + 1
    y = int(cell[1])
    for xy in b:
        x1, y1 = x + xy[1]
        if 0 < x1 < 9 and 0 < y1 < 9:
            print(f'{a[x1 - 1]}{y1}')
