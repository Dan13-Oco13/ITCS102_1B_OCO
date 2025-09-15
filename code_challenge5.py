print("THE FACTORIAL PROGRAM")

number = eval(input("Enter any number ---> "))
factorial = 1
for x in range(number, 0, -1):
	#rint(x)
	factorial *= x
print("the factorial of ",number," is",factorial)