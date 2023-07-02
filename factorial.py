#factorial iterative method
def factroial_iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    return fac
num=int(input("Enter number: "))
print("factrioal iterative method ",factroial_iterative(num))

#factrioal recursive method
def factroial_recursive(n):
    if n==1:
        return 1
    else:
        return n*factroial_recursive(n-1)
print("factrioal recursive method ",factroial_recursive(num))

#quiz
#fibonacci series // 0 1 1 2 3 5 8 13
def fibonacci(n):
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(num))




