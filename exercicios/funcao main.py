def quociente(x, y):
    q = 0
    while x >= y:
        x -= y
        q += 1
        return q

def main():
    a = int(input('a: '))
    b = int(input('b: '))
    q = quociente(a, b)
    print(f'{a} // {b} = {q}')

main()
