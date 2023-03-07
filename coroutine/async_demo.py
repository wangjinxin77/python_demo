import asyncio

# async 用来声明协程（或者称为异步函数）
async def fun1(a, b):
    print(a)
    # await 后面只能跟 可等待对象，包括：协程，任务，future
    # await 表示执行可等待对象，该对象在执行过程中可以被阻塞
    # asyncio.sleep()是一个异步函数，也就是协程。
    # 这里如果没有await，asyncio.sleep()不会被执行，它只会返回一个异步函数对象（即可等待对象）
    await asyncio.sleep(1)
    print(b)


async def fun2(c, d):
    print(c)
    await asyncio.sleep(1)
    print(d)


def async_test():
    fun1_obj = fun1(1, 2)  # 异步函数返回的结果，是异步函数对象，不是函数结果。这个跟同步函数不同
    fun2_obj = fun2(3, 4)

    tasks = [asyncio.ensure_future(fun1_obj),
    asyncio.ensure_future(fun2_obj)]

    loop = asyncio.get_event_loop()
    loop.run_until_complete(asyncio.wait(tasks))  # 列表不是可等待对象，需要加asyncio.wait()


if __name__ == '__main__':
    async_test()
