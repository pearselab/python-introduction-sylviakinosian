#my very own bubble sort
#sorts the list len(list)-1 times

list = [3,112,5,7,15,24,33,49,3,61,2,89]

def bubz(list):
    for j in range(len(list)-1,0,-1):
        for i in range(j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

#quicksort

def quicksort(list):
    bottom = list[0]
    top = list[len(list)-1]
    if bottom < top:
        pivot = partition(list, bottom, top)
        quicksort(list, bottom, pivot-1)
        quicksort(list, pivot+1, top)
    #end if
#end function

def swap(x, y):
    x, y = y, x
    return x, y

def partition(list, bottom, top):
    pivot = top
    x = bottom
    for i in range(0, len(list)):
        if list[i] < pivot:
            swap(list[i], list[x])
            x = x + 1
        #end if
    #end for
    return x
#end function


