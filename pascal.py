
# n=int(input("enter the row number:"))
# list1=[]
# for i in range(n):
#     temp_list=[]
#     for j in range(i+1):
#         if j==0 or j==i:
#             temp_list.append(1)
#         else:
#             temp_list.append(list1[i-1][j-1]+list1[i-1][j])
#     list1.append(temp_list)
# print(list1)
# print("In triangle form:\n")
# for i in range(0,n):
#     for j in range(n-i-1):
#         print(" ",end='')
#     for j in range(i+1):
#         print(list1[i][j],end=' ')
#         print()
#PROGRAM TO SORT ARRAY WITH SQUARES:
a=[-3,4,2,-1,0,-5]
a.sort()
res=[]
i=0
j=len(a)-1
while i<=j:
    if(a[i]*a[i]>=a[j]*a[j]):
        res.append(a[i]*a[i])
        i+=1
    else:
        res.append(a[j]*a[j])
        j-=1
print(res[::-1])