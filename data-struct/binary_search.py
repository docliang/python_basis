def binary_search(mylist,item):
    low = 0
    high = len(mylist)-1
    while low < high:
        mid = (low + high)/2
        guess = mylist[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1
    return None

