# Sales Data Analysis

# Returns two lists
def getIDs(filename):
    IDs = open(filename, "r")
    id_list = []
    sales_data = []
    
    for line in IDs:
        id_list.append(line.strip())
    
    id_list.sort()
    IDs.close()
    return id_list, sales_data

def process_sales_data(filename, id_list, sales_data): 
    data = open(filename, "r")
    row = data.readlines()
    n = 0
    
    # Iterates through all sales IDs
    for i in range(6):
        # Creates 2D list element of quarterly earnings to be appended
        element = [0.00, 0.00, 0.00, 0.00]
        
        for column in row:
            if (column.split(" ")[0]) == (id_list[n]):
                
                # Sorts earnings by quarter
                if int(column.split(" ")[1]) <= 3:
                    x = (element[0]) + (float((column.split(" ")[2]).strip()))
                    element[0] = round(x, 2)
                    
                elif int(column.split(" ")[1]) <= 6:
                    x = (element[1]) + (float((column.split(" ")[2]).strip()))
                    element[1] = round(x, 2)
                    
                elif int(column.split(" ")[1]) <= 9:
                    x = (element[2]) + (float((column.split(" ")[2]).strip()))
                    element[2] = round(x, 2)
                    
                else:
                    x = (element[3]) + (float((column.split(" ")[2]).strip()))
                    element[3] = round(x, 2)
                    
        total = round(sum(element), 2)
        element.append(total)
        element.insert(0, id_list[i])
        sales_data.append(element)
        
        # ID Tracker Index
        n += 1
        
    data.close()

# Generates entire sales report
def print_report(id_list, sales_data):
    # Generates lists for arithmetic
    q1_list = []
    q2_list = []
    q3_list = []
    q4_list = []
    totals_list = []
    gross_sum = []
    
    # Populates lists above for each salesperson
    for i in sales_data:
        q1_list.append(i[1])
        q2_list.append(i[2])
        q3_list.append(i[3])
        q4_list.append(i[4])
        totals_list.append(i[5])
        
        # Iterating through valid figures, excluding ID numbers
        for j in i[1:-1]:
            gross_sum.append(j)
         
    # Generates sum values
    total1 = round(sum(q1_list), 2)
    total2 = round(sum(q2_list), 2)
    total3 = round(sum(q3_list), 2)
    total4 = round(sum(q4_list), 2)
    overall = round(sum(totals_list), 2)
    
    new_element = [total1, total2, total3, total4]
    max_quarter = max(new_element)
    
    quarter_num = new_element.index(max_quarter)
    new_element.insert(0, "Total") 
    new_element.append(overall)
    max_individual = max(gross_sum)
    
    best_ID = 0
    for i in sales_data:
        # Checks the highest performer
        if max_individual in i:
            best_ID = i[0]
    
    sales_data.append(new_element)
    
    # Title Element
    print("--------Annual Sales Report--------")
    sales_data.insert(0, ["ID", "QT1", "QT2", "QT3", "Q4", "Total"])
    
    for line in sales_data:
        # Generates report; prints element in 2D list on separate lines
        for z in line:
            print("{0:<10}".format(z), end = "")
        print()
    print()
    
    print("Max sales by Salesperson: ID = " + str(best_ID) + 
          ", Amount = " + str(max_individual))
    print("Max sales by Quarter: Quarter = " + str(quarter_num + 1) + 
          ", Amount = " + str(max_quarter))

def main():
    s_ids = input("Enter the name of the sales ids file: ")
    s_data = input("Enter the name of the sales data file: ")
    
    x, y = getIDs(s_ids)
    process_sales_data(s_data, x, y)
    print_report(x, y)

# Run the program
main()
