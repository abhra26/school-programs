
#factorial of a number
def factorial(n):
    if n == 0:
        return 1
    else:
        return n*factorial(n-1)
for k in range(2):
    n = int(input('enter number:'))
    if n<0:
        n = int(input('enter positive number:'))
    print('factorial of {0} is {1}'.format(n,factorial(n)))
print('_'*50)
print()

#################################################################
#binary search
def search(l,x, start, end):
    mid = int((start+end)/2)
    if end<start:
        return (x,'is not present')
    elif l[mid]==x:
        return (x,'is present')
    elif x<l[mid]:
        end = mid-1
        return search(l,x,0,end)
    elif x>l[mid]:
        start = mid+1
        return search(l,x,start,end)

for k in range(2):
    l = eval(input('enter list:'))
    l.sort()
    x = int(input('enter number: '))
    end = len(l) - 1
    print(search(l,x,0,end))

print('_'*50)
print()

#############################################################################

#GCD

def gcd(a,b):
    if b == 0:
        return a
    else:
        return gcd(b,a%b)

for k in range(2):
    a = int(input('enter num1:'))
    b = int(input('enter num2:'))

    if a>b:
        print(f'gcd of {a} and {b} is {gcd(a,b)}')
    else:
        print(f'gcd of {a} and {b} is {gcd(b,a)}')

print('_'*50)
print()
#############################################################################

#krishnamurty number
def krishnum(n):
    def calc(n,i=0):
        import math
        if i == len(n):
            return 0
        else:
            return math.factorial(int(n[i]))+calc(n,i+1)
    if calc(n)==int(n):
        return f'{n} is a krishnamurty number'
    else:
        return f'{n} is not a krishnamurty number'
for k in range(2):
    print(krishnum(input('enter numb:')))

print("_"*50)
print()
################################################################3
# combination program c(n,r)

def C(n,r):
    import math
    a = n
    b = r
    c = n-r
    def permutation(n, r):
        if r == 1:
            if n != 1:
                return n * permutation(n - 1, 1)
            else:
                return 1
        else:
            return (n / r) * permutation(n - 1, r - 1)

    if n == 0:
        return 1
    else:
        return permutation(a,c)/math.factorial(b)

for k in range(2):
    n = int(input('enter n:'))
    r = int(input('enter r:'))
    print('result of {0}C{1} is {2}'.format(n,r,C(n,r)))