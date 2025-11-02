def merge1(dict1, dict2):
    result = dict(dict1)
    for k, v in dict2.items():
        if k in result:
            result[k] += v
        else:
            result[k] = v
    return result


def merge(f, *dicts):
    result = {}
    for d in dicts:
        for k, v in d.items():
            try:
                result[k] = f(result[k], v)
            except KeyError:
                result[k] = v
    return result


def main():
    res = merge(lambda x,y: x*y, {'a':10, 'b':20}, {'b':3, 'c': 4})
    print(res)

if __name__ == '__main__':
    main()
