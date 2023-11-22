from task_2 import logger

list_of_lists_1 = [
    ['a', 'b', 'c'],
    ['d', 'e', 'f', 'h', False],
    [1, 2, None]
]


@logger(path='generator_log.log')
def flat_generator(list_of_lists):
    counter_list = 0
    len_list_of_lists = len(list_of_lists)
    while counter_list < len_list_of_lists:
        current_list = list_of_lists[counter_list]
        for element in current_list:
            yield element
        counter_list += 1


if __name__ == '__main__':
    test = flat_generator(list_of_lists_1)
    for i in test:
        print(i)