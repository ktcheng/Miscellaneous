# Celsius to Fahrenheit Table

temp = int(input("Enter a number to see the range of temperatures: "))

for c in range(temp + 1):
    f = ((9/5) * c) + 32
    print(c, round(f, 1)) # prints celsius & fahrenheit temperatures
