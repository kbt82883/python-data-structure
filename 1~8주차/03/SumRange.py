def sum_range(begin, end, step = 1):
    sum = 0
    for n in range(begin, end +1 , step):
        sum += n

    return sum

if __name__ == '__main__':
    print(sum_range(end = 10, begin=1))
    