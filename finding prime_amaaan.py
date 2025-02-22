// checking if a number is prime or not, algorithm was suggested by "amaan-123"
x=float(input('enter a number:'))
if x==0 or x==1:
    print(x ,'is neither prime nor composite')
    exit()
if x==2 or x==3 :
    print(x,'is prime')
    exit()
elif x%2==0 or x%3==0:
    print(x,'is not prime')
    exit()
else:
    from math import sqrt
    n=round(sqrt(x))
    for i in range(3,n,2):
        if x%i==0:
            print(x,' is not prime')
            exit()
        else:
            print(x,' is prime')
            exit()
