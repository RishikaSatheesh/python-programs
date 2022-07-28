# Example:a= 5 4 10 1 6 2 
# a[0]= sorted sublist, rest is unsorted sublist. 
# store 4 in temp var in temp and make a hole at that position.
# compare val at temp with sorted sublist. Since 5>4, shift 5 to the right with one.
# We reached end of sorted sublist. SO put val of temp on sorted sublist.
#  Now: 4 5 10 1 6 2
#  4 5 : sorted sublist
#  temp=10. Compare the sorted sublist. Both are lesser than 10. so  enter 10 back in position.
#  4 5 10 : sorted sublist
#  1 6 2 : unsorted sublist
#   4 5 10 | _ 6 2 - compare 1 to 10. shift 10 to right.
#   5>1 so 5 is shifted to the right. 
#   4 _ 5 10 6 2 
#   1 4 5 10| 6 2 : Now 6.
#   1 4 5 6 10 |2
#   1 2 4 5 6 10 : Sorted List

#Implementing Insertion Sort:
from tkinter import N


def insertionSort(A):
    n=len(A)
    for i in range(1,n):
        temp=A[i]
        position=i
        while position>0 and A[position-1]>temp:
            A[position]=A[position-1]
            position=position-1
        A[position]=temp

A=[5,4,10,1,6,2]
print("Unsorted Array: ",A)
insertionSort(A)
print("Sorted Array :",A)



