def printHeader(n):
    print('   ', end='')

    for c in range(1, n + 1):
        print(f'  {c}  ', end='')

    print()
    print('  ', end='')
    for c in range(1, n + 1):
        print('-----', end='')

    print()


def multiTable(n):
    printHeader(n)

    for r in range(1, n + 1):
        # %2d formata o espaço para reservar 2
        # % r é para identificar a variavel r do for
        print('%2d |' % r, end='')
        for c in range(1, n + 1):
            # %3d formata o espaço para reservar 3 
            print('%3d  ' % (r * c), end='') 

        print()

n = int(input('Enter a number: '))

multiTable(n)
