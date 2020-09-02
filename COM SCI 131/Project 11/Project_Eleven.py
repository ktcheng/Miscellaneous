# Windchill

# Opening Statement
print("This program calculates the windchill from the fahrenheit " + 
      "temperature and the wind speed.")

def get_input():
    t = float(input("Enter the fahrenheit temperature:"))
    v = float(input("Enter the wind speed:"))
    return t, v

def calculate_windchill(temperature, wind_speed):
    w = (35.74 + 0.6215 * (temperature) - 35.75 * (wind_speed**0.16) + 
         0.4275 * temperature * (wind_speed**0.16)) # Windchill formula
    windchill = round(w, 1)
    return windchill

while True:
    t, v = get_input()
    w = calculate_windchill(t, v)
    
    print("The windchill is:", str(w))
    x = input("Would you like to calculate another windchill?" + 
              " Enter 'y' or 'n': ")
    
    if x == "n":
        break
