a=int(input("Enter a first number:"))
b=int(input("Enter a Second number:"))
op=input("Enter a operator(+,-,*,/):"))
if op=="+":
    print("Result=",a+b)
elif op=="-":
    print("Result=",a-b)
elif op=="*":
    print("Result=",a*b)
elif op=="/":
    print("Result=",a/b)
else:
    print("Invalid")
