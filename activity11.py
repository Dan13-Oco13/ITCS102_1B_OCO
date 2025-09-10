temp = eval(input("Enter the temperature --> "))

if temp <= 0 :
	print("Temperature is Considered as BELOW FREEZING")

elif temp >= 1 and temp <= 15 :
	print("Temperature is Considered as Extremely cold")

elif temp >= 16 and temp <= 30 :
	print("Temperature is Considered as Cold Temperature")

elif temp >= 31 and temp <= 38 :
	print("Temperature is Considered as Lukewarm Temperature")

elif temp >= 39 and temp <= 42 :
	print("Temperature is Considered  as Warm Temperature")

elif temp >= 43 and temp <= 50 :
	print("Temperature is Considered as Hot Temperature")

elif temp >= 51 and temp <= 60 :
	print("Temperature is Considered as  Extremely Hot Temperature")

elif temp >= 61 :
	print("Temperature is Considered as Burning Temperature")

#else:
#	print("Invalid Temperature")
	