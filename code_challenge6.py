print("ODD NUMBER SUMMATION")

base = 0
for number in range(7):
	user = eval(input("What are your numbers? " ))
	check = user % 2
	if check != 0:
		base += user
if base != 0:
	print("The total sum of your odd numbers are:", base)
else:
	print("You entered all even numbers")