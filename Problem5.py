import matplotlib.pyplot as plotting
from math import *
inp = input("Enter an equation for x(n): ")
def X(n):
    return eval(inp) 
def Y(n): 
    if n==0: 
        value1= -1.5*X(n)+2*X(n+1)-0.5*X(n+2)
        return value1
    elif n>0 and n<=198: 
        value2= 0.5*X(n+1)-0.5*X(n-1)
        return value2
    elif n==199: 
        value3= 1.5*X(n)-2*X(n-1)+0.5*X(n-2)
        return value3
numbers = list(range(0,200))
x=[X(n) for n in numbers] 
y=[Y(n) for n in numbers] 
plotting.legend
plotting.plot(numbers,y,'b', label = 'y(n)') 
plotting.plot(numbers,x,'r',label = 'x(n)') 
plotting.xlabel('Values of n') 
plotting.ylabel('Values of x(n) and y(n)') 
plotting.legend() 
plotting.show