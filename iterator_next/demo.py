from collections import abc
import pysnooper

# 只要实现__iter__(), 或者实现__getitem__()并且__getitem__()的参数index是从0开始的
# 这个类就是广义的可迭代的。用iter()来检查，有异常则不是
# 狭义的可迭代的，是必须实现__iter__()。用isinstance(a, abc.Iterable)来检查，返回False，则不是
class IteratedWords:
    def __init__(self, text):
        self.words = text.split(" ")

    def __getitem__(self, index):
        return self.words[index]


# 下面这个类虽然是狭义的可迭代的，但__iter__()返回的对象没有实现__next__(), 所以用for 循环是会报错的
# 因为for循环会首先默认调用iter()该对象
# 由于它没有__next__()， 它也不是迭代器。
class IteratedWordsIter:
    def __init__(self, text):
        self.words = text.split(" ")
        self.text = text

    def __iter__(self):
        return self

    # def __iter__(self):
    #     return IteratorWords(self.text)


def test_iterated():
    ite = IteratedWords('I am a coder')
    for word in ite:
        print(word)

    print("=====get by index====")
    print(ite[0])
    print(ite[2])
    # print(next(a))  #没有实现__next__(), 不能用next()
    print("=====get by iter() and next()====")
    # 能用for的，都是可迭代的； 能用next()都是迭代器。
    # 但可迭代的却不一定都能用for，比如上面的类只实现__iter__(),但__iter__()返回的对象却没有__next__() 
    print(isinstance(ite, abc.Iterable))
    print(isinstance(ite, abc.Iterator))
    a=iter(ite)  # 检查广义可迭代，同时获取迭代器的对象
    print(next(a))
    print(next(a))
    print(isinstance(a, abc.Iterable))  # 当没有__iter__(), isinstance(a, abc.Iterable)会是False
    print(isinstance(a, abc.Iterator))


def test_iterated_only_iter():
    ite = IteratedWordsIter('I am a iterable object with only __iter__')
    print(isinstance(ite, abc.Iterable))
    print(isinstance(ite, abc.Iterator))
    for word in iter(ite):
        print(word)


# 标准迭代器必须实现下面两个方法
# __iter__(),  return self
# __next__(),  返回下一个元素，没有抛出StopIteration异常
class IteratorWords:
    def __init__(self, text):
        self.words = text.split(" ")
        self.index = 0

    def __iter__(self):
        return self

    # @pysnooper.snoop()
    def __next__(self):
        if self.index >= len(self.words):
            raise StopIteration

        self.index += 1
        return self.words[self.index - 1]


def test_iterator():
    ite = IteratorWords('I am a iterator')
    print(f'>>ite type: {type(ite)}')
    for word in ite:
        print(word)

    print("=====get by index====")
    # print(ite[0])  #TypeError: 'IteratorWords' object is not subscriptable, 没有实现__getitem__, 不可下标访问
    print("=====get by iter() and next()====")
    a=iter(ite)
    # a=iter(IteratorWords('I am a iterator'))
    print(f'>>ite type: {type(ite)}, iter(ite) type: {a}')
    print(next(a))  # 用完上面的for后，不能用next()。换句话说，for 和next()不能混用
    print(next(a))
    print(isinstance(ite, abc.Iterable))
    print(isinstance(ite, abc.Iterable))
    print(isinstance(a, abc.Iterable))
    print(isinstance(a, abc.Iterator))


def test_iter_set():
    a = (n for n in range(9))
    for n in a:
        print(n)
    print(f'a type: {type(a)}')  # 结果 a type: <class 'generator'> 
    b = (n for n in [1,2,3])
    print(f'b type: {type(b)}')  # 结果 b type: <class 'generator'>
    c = {n for n in range(9)}
    print(f'c type: {type(c)}')  # 结果 c type: <class 'set'> 
    d = {n: n*n for n in range(9)}
    print(f'd type: {type(d)}')  # 结果 d type: <class 'dict'>
  
 

if __name__ == '__main__':
    # test_iterator()
    # test_iterated_only_iter()
    test_iter_set()
