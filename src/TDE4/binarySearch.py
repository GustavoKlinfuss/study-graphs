

def b_search(array, element):
    start = 0
    end = len(array) - 1

    while end >= start:
        mid = (end + start)//2
        if array[mid] == element:
            return mid
        elif array[mid] < element:
            start = mid + 1
        elif array[mid] > element:
            end = mid - 1
    return - 1
