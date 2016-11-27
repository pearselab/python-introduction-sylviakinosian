#my very own bubble sort
#sorts the list len(list)-1 times

list = [3,112,5,7,15,24,33,49,3,61,2,89]

def bubz(list):
    for j in range(len(list)-1,0,-1):
        for i in range(j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

#quicksort sorts quickly

def swap(x, y):
    x, y = y, x
    return x, y

def partition(list):
    top = list[len(list)-1]
    bottom = list[0]
    pivot = top-1
    x = bottom
    for i in range(bottom,(top-1)):
        if list[i] < pivot
            swap(list[i], list[x])
            x = x + 1
        end
        iffffffffffffffffffffffffffffffffffffffffffffvvvvvv                                        ffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff
