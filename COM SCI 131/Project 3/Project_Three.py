# Software Sales Calculator

num_packages = input("Enter the number of packages you ordered: ")

# Conditional prints price & discount at 2 decimal places
if int(num_packages) >= 100:
    
    price = (int(num_packages) * 100)
    discount = price * 0.40
    price = price - discount
    
    print("The total cost of your purchase was $" + "{:.2f}".format(price) + \
          " with a discount of $" + "{:.2f}".format(discount) + ".")
    
elif int(num_packages) >= 50:
    
    price = (int(num_packages) * 100)
    discount = price * 0.30
    price = price - discount
    
    print("The total cost of your purchase was $" + "{:.2f}".format(price) + \
          " with a discount of $" + "{:.2f}".format(discount) + ".")
    
elif int(num_packages) >= 20:
    
    price = (int(num_packages) * 100)
    discount = price * 0.20
    price = price - discount
    
    print("The total cost of your purchase was $" + "{:.2f}".format(price) + \
          " with a discount of $" + "{:.2f}".format(discount) + ".")
    
elif int(num_packages) >= 10:
    
    price = (int(num_packages) * 100)
    discount = price * 0.10
    price = price - discount
    
    print("The total cost of your purchase was $" + "{:.2f}".format(price) + \
          " with a discount of $" + "{:.2f}".format(discount) + ".")
    
elif int(num_packages) >= 0:
    
    price = (int(num_packages) * 100)
    discount = price * 0.00
    price = price - discount
    
    print("The total cost of your purchase was $" + "{:.2f}".format(price) + \
          " with a discount of $" + "{:.2f}".format(discount) + ".")
    
else: 
    # positive integer validation check
    print("Please enter a valid number for the number of packages purchased.")
