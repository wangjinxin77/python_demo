#

# 生成器函数
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


def numb(n):
    i = 0
    while i < 10:
        n += i
        print(f'before >>n: {n}')
        a = yield n
        i += 1
        print(f'after >>n: {n}, a: {a}')


# test next() 和list
def test():
    a = sum(1)
    next(a)
    next(a)
    #next(a)
    #next(a)
    #print(f'>>sum list:{[b for b in a]}')


# test send()
def test_numb():
    b = numb(0)
    next(b)
    next(b)
    b.send(100)
    b.send(200)


# 生成器表达式
def test_generator_expression():
    a = (n for n in range(9))
    for n in a:
        print(n)
    print(f'a type: {type(a)}')  # 结果 a type: <class 'generator'>
    b = (n for n in [1,2,3])
    print(f'b type: {type(b)}')  # 结果 b type: <class 'generator'>


# iterator object with generator function or expression
class IteratorGeneratorFunc:
    def __init__(self, text):
        self.text = text
        self.words = text.split(" ")
# 
#     def __iter__(self):
#         for word in self.words:
#             yield word

    def __iter__(self):
        return (word for word in self.words)


def test_iterator_generator():
    words = IteratorGeneratorFunc('I am a iterator with generator func')
    for word in words:
        print(word)


if __name__ == '__main__':
    # test()
    # test_numb()
    test_iterator_generator()
