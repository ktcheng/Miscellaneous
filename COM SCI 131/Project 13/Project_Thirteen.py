# Grade Average With Exceptions

def calculateAverage(total, count):
    avg = total / count
    return avg

exam_scores = [] 
count = 0

while True:
    z = 0
    while z == 0:
        # Validation Checker
        try:
            score = float(input("Enter a positive number to total " + 
                                "or a negative number to calculate average: "))
            z = 1
        except:
            print("What you entered was not a valid number. Try again.")
    
    if score > 0:
        exam_scores.append(score)

    if score < 0:
        total = sum(exam_scores)
        
        try:
            avg = calculateAverage(total, count)
            print(avg)
        except ZeroDivisionError:
            print("You did not enter any numbers to average.")
        break
    
    count += 1
