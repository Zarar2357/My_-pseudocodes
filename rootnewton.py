# writing a pseudocode to find square root of a number using newtons raphson's method
# tolerence is up to three decimal places
n=int(input('enter the number: '))
x=n/2
p=round(x)
for i in range(1,p):
    w=(x*x+n)/(2*x)
    a=round(1000*x)/1000
    b=round(1000*w)/1000
    if a==b:
        break
    else:
        x=w
print('The square root of ',n,' is ',a)
