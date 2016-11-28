#my very own bubble sort
#sorts the list len(list)-1 times

list = [3,112,5,7,15,24,33,49,3,61,2,89]

def bubz(list):
    for j in range(len(list)-1,0,-1):
        for i in range(j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

#Quicksort
#issues with list indexing

def quicksort(list):
    bottom = list[0]
    top = list[len(list)-1]
    if bottom < top:
        pivot = partition(list, bottom, top)
        quicksort(list, bottom, pivot-1)
        quicksort(list, pivot+1, top)
    #end if
#end function

#do we care about picking a median value for the pivot .. ?
def partition(list, bottom, top):
    pivot = top
    x = bottom
    for i in range(0, len(list)):
        if list[i] < pivot:
            list[i], list[x] = list[x], list[i]
            x = x + 1
        #end if
    #end for
    return x
#end function



