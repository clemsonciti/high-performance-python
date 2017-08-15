def mean(data):
    N = len(data)
    data_sum = 0
    for num in data:
        data_sum += num
    return data_sum/N