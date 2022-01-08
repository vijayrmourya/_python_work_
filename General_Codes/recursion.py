def flatten(list_of_lists):
    print(list_of_lists)
    if len(list_of_lists) == 0:
        return list_of_lists
    if isinstance(list_of_lists[0], list):
        return flatten(list_of_lists[0]) + flatten(list_of_lists[1:])
    return list_of_lists[:1] + flatten(list_of_lists[1:])


print(flatten([1, 2, [3], [[4]], [[[5]]]]))