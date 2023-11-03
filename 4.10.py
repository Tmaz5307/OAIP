message = input()
for i in range(len(message)):
    if message[i] == ' ' or i % 2 == 0:
        print(message[i], sep='', end='')
