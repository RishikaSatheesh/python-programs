def fib(n):
    if n==0 or n==1:
        return n
    else:
        return(fib(n-1)+fib(n-2))
t=int(input("How many terms in Fibonacci Series do you want?"))
if(t<=0):
    print("Error.\nOnly positive no.s are accepted.\n")
else:
    print("Fibonacci Sequence:\n")
    for i in range(t):
        print(fib(i))