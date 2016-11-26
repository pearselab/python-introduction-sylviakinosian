#my very own bubble sort

#sorts the list len(list)-1 times
def bubz(list):
    for j in range(len(list)-1,0,-1):
        for i in range(j):
            if list[i] > list[i+1]:
                list[i], list[i+1] = list[i+1], list[i]
    return list

#quicksort

#partition
