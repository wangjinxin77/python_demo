
out_id = 0


def out_yield():
    global out_id
    print(f'start out_yield: out_id {out_id}')
    for i in range(3):
        out_id += 1
        resp = yield out_id
        print(f'out_yield: i {i}, out_id {out_id}, resp {resp}')
    return out_id, resp


def yield_test():
    # print([i for i in out_yield()])
    out2 = out_yield()
    print(f'yield_test begin 1th next out2: {next(out2)}')
    print(f'yield_test begin 2th next out2: {next(out2)}')
    print(f'yield_test begin 1th out2 send 100: {out2.send(100)}')
    print(f'yield_test begin 2th out2 send 101: {out2.send(101)}')


# yielf from 用于嵌套生成器函数
# yielf from只是一个传输管道，传输子生成器函数里所有的yield
def out_yield_from():
    print(f'start out_yield_from: out_id {out_id}')
    for i in range(100, 101):
        # 只有out_yield()结束了，才会把return的值给resp_out_id, resp
        resp_out_id, resp = yield from out_yield()
        print(f'in out_yield_from: out_id {resp_out_id}, resp {resp}')


def yield_from_test(): 
    # print([i for i in out_yield_from()])
    get_out = out_yield_from()
    print('start yield_from_test(): begin next=====')
    next(get_out)
    print('start yield_from_test(): end next=====')
    for i in range(3):
        get_out.send(1000 + i + 1)


def out_yield_from_from():
    print(f'start out_yield_from_from: out_id {out_id}')
    for i in range(2):
        yield from out_yield_from()


def yield_from_from_test(): 
    print([i for i in out_yield_from_from()])



if __name__ == '__main__':
    #yield_test()
    yield_from_test()
    #yield_from_from_test()
