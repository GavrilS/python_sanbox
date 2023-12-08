

TEST_LIST_ITEM = [
    'Iris', 'Orchids', 'Rose', 'Lavender', 'Lily', 'Carnations', 'Sun', 'Sunflower'
]


def copy_items(list_to_copy):
    return list_to_copy[:]


def remove_list_items(list_items):
    print('original list: ', list_items)
    print('*'*40)

    test_list = copy_items(list_items)
    print('Removing items from list:')
    print('*'*40)

    print('using Del()')
    del test_list[1]
    print('del test_list[1]: ', test_list)
    print('*'*40)

    print('Using List Comprehension')
    test_list = [x for x in test_list if not x.startswith('I')]
    print('test_list: ', test_list)
    print('*'*40)

    print('using pop()')
    a = test_list.pop(0)
    print('Item removed: ', a)
    print('test_list: ', test_list)
    print('*'*40)

    print('using filter()')
    test_list = list(filter(lambda item: item!='Lily', test_list))
    print('after filtering Lily: ', test_list)
    print('*'*40)

    print('using slicing: ')
    test_list = test_list[:2]
    print('test_list[:2]: ', test_list)
    print('*'*40)

    print('using remove()')
    for item in test_list:
        test_list.remove(item)
        break
    
    print('Final test_list: ', test_list)



if __name__=='__main__':
    remove_list_items(TEST_LIST_ITEM)
