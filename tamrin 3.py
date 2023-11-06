avg = 0

while avg != 20.0:
    score = input("Enter your score with comma: ")
    
    counter = 0
    scores = score.split(",")
    
    for i in scores:
        counter+= int(i) 
    avg = counter / len(scores)


print("I will buy a bike for you")