import random
def quicksort(lst : list) -> list:
    """Quicksort algorithm"""
    if(len(lst) == 1):
        return [lst[0]]

    pivot = lst[len(lst) - 1]
    left = 0
    right = len(lst) - 1

    while left != right:

        while lst[left] <= pivot and left < right:
            left = left + 1

        found_left = lst[left]
    
        while lst[right] > pivot and right > left:
            right = right - 1

        found_right = lst[right]

        #Swap
        if(found_left != found_right):
            lst[left] = found_right
            lst[right] = found_left


    return quicksort(lst[:left]) + quicksort(lst[right:])


def quicksort(lst : list, pred = lambda x : x) -> list:
    """Quicksort algorithm"""
    if(len(lst) == 1):
        return [lst[0]]

    pivot = pred(lst[len(lst) - 1])
    left = 0
    right = len(lst) - 1

    while left != right:

        while pred(lst[left]) <= pivot and left < right:
            left = left + 1

        found_left = lst[left]
    
        while pred(lst[right]) > pivot and right > left:
            right = right - 1

        found_right = lst[right]

        #Swap
        if(found_left != found_right):
            lst[left] = found_right
            lst[right] = found_left


    return quicksort(lst[:left],pred) + quicksort(lst[right:],pred)

#Example
lst = ["C","B","A"]
pred = lambda x : ord(x)
print(quicksort(lst,pred))

#Example 2
lst = [random.randint(0,100) for _ in range(0,100)]
print(quicksort(lst))
