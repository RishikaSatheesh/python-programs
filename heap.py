import heapq
# li=[3,7,9,1,5]  #list
# print("List is: ",end="")
# print(li)
# heapq.heapify(li)   #coverting list to a minheap
# #printing both list and minheap form of it:

# print("Created minheap: ",end="")
# print(list(li))
# heapq.heappush(li,4)
# print(list(li))
# #print(heapq.heappop(li))

# #heappushpop funcion to push and pop simultaneously
# print(heapq.heappushpop(li,2))  #pushes 2 and pops smallest element
# print(list(li))
# print(heapq.heapreplace(li,7))  #replaces smallest element with new element, that is the smallest element is popped.
# print(list(li)) #prints the newly rearranged elements in a min heap post replacement.


# ##To print k largest numbers from the heap:
# ##nlargest(k,iterable,key=fun)
# print(heapq.nlargest(3,li))
# ##To print k smallest numbers from the heap:
# ##nsmallest(k,iterable,key=fun)
# print(heapq.nsmallest(3,li))
def kthLargest(arr,k):
    arr=[-elem for elem in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)

arr=[3,6,2,1,7,8,9]
print(kthLargest(arr,2))