#ask user to input 10(ten) numbers 
#after get the summation of all numbers

sum = 0
for d in range(1, 6, 1,):
	print(d)
	number = eval(input("Enter anything ---> "))
	sum += number
print("The sum of all the numbers ",sum)