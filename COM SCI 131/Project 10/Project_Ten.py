# Falling Distance

# Opening Statement
print("This program tells you how far an object will fall in a number of" + 
      " seconds.")

def fallingDistance():
    time = float(input("Enter the falling time in seconds: "))
    distance = 0.5 * 9.8 * (time**2) # Kinematics equation
    d = round(distance, 1)
    return d, time

while True: 
    d, time = fallingDistance()
    if float(time) < 0: # Entering a negative number will break
        break
    
    print("The distance the object will fall in", str(time), "seconds, is:",
          str(d), "meters.")
