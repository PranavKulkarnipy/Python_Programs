# fiboacci series using recursion

def fibo(n):
    if n<=1:   # base case termination cas
        return n
    return fibo(n-1)+ fibo(n-2) # recursive function

n=int(input("Enter a number for fiboncci"))
if n<0:
    print("please enter positive number")
else:
    for i in range(n):
        print(fibo(i))



    

    """"
    fibo(5)
 fib(5)=    fibo(5-1)+fibo(5-2)   fibo(4)+fibo(3)  fibo(4)=3  fibo(3)=2          fibo(5)=3+2=5
 return fibo(5)=5   



 
 fibo(4) =  fibo(4-1)+ fibo(4-2)  fibo(3)+fibo(2)  fibo(3)=2  fibo(2)=1
 fibo(4)=2+1=3 
 return fibo(4)=3 
 
 
 
 fibo(3)=   fibo(3-1)+ fibo(3-2)   fibo(2)+fibo(1)  fibo(2)=1  fibo(1)=1         fibo(3)=1+1=2  
 return fiobo(3)=2    
 
 
 fibo(2)=   fibo(2-1)+ fibo(2-2)   fibo(1)+ fibo(0)  fibo(1)=1  fibo(0)=0     fibo(2)=1+0=1    
 return fibo(2)=1 
 
 
 fibo(1)= 1  return 1

 fibo(0)=0   return 0


 starting return value  form fibo(1) when condition reach to  base case temination case when  it reached to fibo(1) 
fibo(-1) no consider because of if n<0:  please enter positive number


Each recursive call creates a new instance of the function on the call stack:

When a function calls itself within its own definition, it effectively creates a new instance of the function, with its own set of local variables and arguments.
This new instance is pushed onto the call stack, a temporary memory area that keeps track of the program's current execution state.
You can think of it as a stack of plates, where each new function call adds a new plate on top of the stack.
During recursion, execution of each function is paused until the current recursive call returns:

When a function makes a recursive call, its own execution is temporarily suspended, and the function's state (local variables, arguments) is stored on the call stack.
Once the base case is reached (the condition that terminates the recursion), the function starts returning values.
As the recursive calls return, the suspended functions resume execution, using the returned values to complete their operations.

    """
    