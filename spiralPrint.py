
# The program takes in the number of test cases in the first line of input.
# This is followed by space-separated values of m,n, and s that indicate the number of rows, columns, and length of string respectively.
# The following line is the string of length 's' that needs to be inserted spirally inward into a matrix.
# The output of each test case will be the matrix with the required string entered spirally.

t=int(input())
i=0

while(i!=t):
    test=list(map(int,input().split()))
    string=input()
    m=test[0]
    n=test[1]
    s=test[2]
    top=0
    bottom=m-1
    left=0
    right=n-1
    dir=0
    j=0
    matrix=[[None for h in range(n)] for l in range(m)]
    while top<=bottom and left<=right:
        if dir==0: #left to right
            for k in range(left,right+1):
                matrix[top][k]=string[j]
                j=(j+1)%s
            top+=1
        elif dir==1:
            for k in range(top,bottom+1):
                matrix[k][right]=string[j]
                j=(j+1)%s
            right-=1
        elif dir==2:
            for k in range(right,left-1,-1):
                matrix[bottom][k]=string[j]
                j=(j+1)%s
            bottom-=1
        elif dir==3:
            for k in range(bottom,top-1,-1):
                matrix[k][left]=string[j]
                j=(j+1)%s
            left+=1
        dir=(dir+1)%4

    i+=1
    for g in range(m):
        for v in range(n):
            print(matrix[g][v],end=' ')
        print()
