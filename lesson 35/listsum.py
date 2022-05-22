def sum_list(lis: list) -> int:
    """finds sum of nums in list"""
    result = 0
    if len(lis) == 1 and str(type(lis[0])) == "<class 'int'>":
        return lis[0]
    for i in lis:
        if str(type(i)) == "<class 'int'>":
            lis.remove(i)
            result += i
        if str(type(i)) == "<class 'list'>":
            lis.remove(i)
            for s in i:
                lis.append(s)
    try:
        lis[0] += result
    except TypeError:
        lis.append(result)
    return sum_list(lis)


print(sum_list([2, 3, [1, 2], [4, 5, [10, 1]]]))
