# writing a program to find maximum of three numbers
a=input("Enter the first number: ")
b=input("Enter the second number: ")
c=input("Enter the third number: ")
if a==b and b==c:
    print('a+b+c')
elif a>b and a>c:
    print("The maximum number is: ", a)
elif b>a and b>c:
    print("The maximum number is: ", b)
else:
    print("The maximum number is: ", c)
