name=input("Enter Student name:")
mark1=int(input("Enter mark 1:"))
mark2=int(input("Enter mark 2:"))
mark3=int(input("Enter mark 3:"))
total=mark1+mark2+mark3
average=total/3
print("Student Name:",name)
print("Total Marks:",total)
print("Average:",round(average,2))
if average>=50:
    print("Result: Pass")
else:
    print("Result:Fail")
