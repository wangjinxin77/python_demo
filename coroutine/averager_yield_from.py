import pysnooper
from collections import namedtuple

Result = namedtuple('Result', 'count average')


def averager():
    total = 0.0
    count = 0
    average = None
    while True:
        term = yield
        if term is None:
            break
        total += term
        count += 1
        average = total/count
    return Result(count, average)


# @pysnooper.snoop()
def grouper(count):
    print(f">>>run grouper here {count}th before")
    result = yield from averager()
    print(f">>>run grouper here {count}th after")
    return result


# @pysnooper.snoop()
def grouper_while(results, key):
    count = 0
    while True:
        count += 1
        results[key] = yield from grouper(count)
    print(f">>>run grouper here end: {count}th")


def main(data):
    results = {}
    for key, values in data.items():
        group = grouper_while(results, key)
        next(group)
        for value in values:
            group.send(value)
        group.send(None)
    print(results)


data = {
    "girls;kg": [40.9, 38.5, 44.3, 42.2, 45.2, 41.7, 44.5, 38.0, 40.6, 44.5],
    "girls:m": [1.6, 1.51, 1.4, 1.3, 1.41, 1.39, 1.33, 1.46, 1.45, 1.43],
    "boys:kg": [39.0, 40.8, 43.2, 40.8, 43.1, 38.6, 41.4, 40.6, 36.3],
    "boyrs:m": [1.38, 1.5, 1.32, 1.25, 1.37, 1.48, 1.25, 1.49, 1.46]
}


if __name__ == "__main__":
    main(data)

