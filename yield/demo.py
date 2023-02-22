#

def sum(n):
    i = 0
    print('====start:')
    if n == 0:
        return
    while i<10:
        n += i
        i += 1
        print(f'before>>n: {n}, i:{i}')
        yield n
        print(f'after>>n: {n}, i:{i}')

def test():
    a = sum(1)
    next(a)
    next(a)
    #next(a)
    #next(a)
    #print(f'>>sum list:{[b for b in a]}')


if __name__ == '__main__':
    test()
