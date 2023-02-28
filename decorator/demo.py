def d1(func):
    print(f'run d1 before run __main__')
    return func

def d2(func):
    def decorate(*args):
        print(f'run d2 in decorate {func.__dict__}')
        func(*args)
    return decorate


# below code same as
# test_func = d1(d2(test_func))
@d1
@d2
def test_func(text):
    print(f'run test_func: {text}')


registry = set()
def d3_with_args(active=False):
    def decorate3(func):
        if active:
            registry.add(func)
        else:
            registry.discard(func)
        print(f'run decorate3: registry {registry}')
        return func
    return decorate3


@d3_with_args(True)
def test_func3(text):
    print(f'run test_func3: {text}')

if __name__ == '__main__':
    print(">>>>begin test:")
    test_func('runing text')

    
