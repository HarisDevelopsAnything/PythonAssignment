import temperature_converter as tc
print("1) Celsius to Kelvin")
print("2) Celsius to Fahrenheit")
print("3) Fahrenheit to Kelvin")
print("4) Fahrenheit to Celsius")
print("5) Kelvin to Celsius")
print("6) Kelvin to Fahrenheit")
ch= int(input("Enter your choice: "))
temp= float(input("Enter the temperature: "))
if ch==1:
	print(f"{temp} degree celsius in kelvin: {tc.ctok(temp)}")
elif ch==2:
	print(f"{temp} degree celsius in fahrenheit: {tc.ctof(temp)}")
elif ch==3:
	print(f"{temp} degree fahrenheit in kelvin: {tc.ftok(temp)}")
elif ch==4:
	print(f"{temp} degree fahrenheit in celsius: {tc.ftoc(temp)}")
elif ch==5:
	print(f"{temp} kelvin in celsius: {tc.ktoc(temp)}")
elif ch==6:
	print(f"{temp} kelvin in fahrenheit: {tc.ktof(temp)}")