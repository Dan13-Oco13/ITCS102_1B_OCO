name = input("Enter your name:") 

fare = float(input("Enter your fee:"))

student = input("Are you a student? (yes/no): ")

if student == "yes":
	discount = fare * 0.20
	discounted_price = fare - discount

	print("Hello", name)
	print("Your discount is:", discount)
	print("Your discounted fare is:", discounted_price)
else:
	print("Hello",name)
	print("Your are not eligible for a discount.")
	print("Your fare is:", fare)
