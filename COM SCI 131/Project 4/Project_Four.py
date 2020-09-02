# Grade Average

n = 0
exam_scores = []

while True:
    score = float(input("Enter a test score, enter -1 to see average: "))
    exam_scores.append(score)
    n += 1
    
    if float(score) == -1:
        avg = float((sum(exam_scores) + 1) / (n-1))
        print(avg)
        break
