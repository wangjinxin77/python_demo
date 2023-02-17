# coding=utf8
from contextlib import contextmanager


class ContextObject(object):
    def __enter__(self):
        print('__enter__')
        return self

    def __exit__(self, exc_type, exc_value, exc_tb):
        print(f'__exit__: {exc_type} {exc_value} {exc_tb}')
        return True

    def set_property(self, prop):
        print(f'set_property: {prop}')


def test_with():
    with ContextObject() as context:
        print('test in context:')
        context.set_property('good')


@contextmanager
def demo_contextmanager():
    print('simulate __enter__')
    try:
        yield 'simulate set_proprety'
    finally:
        print('simulate __exit__')


def test_contextmanager():
    with demo_contextmanager() as context:
        print(context)


if __name__ == "__main__":
    test_with()
    test_contextmanager()

