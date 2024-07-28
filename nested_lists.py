def sort_students(names_scores):
    scores = []
    for student in names_scores:
        scores.append(student[1]) #Append the scores in scores list. The [1] is about only the scores
    
    sorted_scores = sorted(set(scores)) #The scores duplicated was exclued and sorted
    second_lowest = sorted_scores[1]
    
    ##### The last part is find the students with duplicated scores
    
    names_second_lowest =[]
    for student in names_scores:
        if student[1] == second_lowest:
            names_second_lowest.append(student[0])
    names_second_lowest = sorted(names_second_lowest)
    
    for name in names_second_lowest:
        print(name)


#Execution list
if __name__ == '__main__':
    names_scores =[] # Created a list to input the name and scores below
    for _ in range(int(input())): # Ask how many students we have to 
        name = input()
        score = float(input())
        names_scores.append([name, score])
    
    sort_students(names_scores)
        
        