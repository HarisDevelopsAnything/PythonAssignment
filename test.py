def calcScore(students,marks):
        for i in range(5):
            print(f"Answers of {students[i]}:")
            for j in range(4):
                inp= input(f"Enter the answer for question {j+1}: ")
                if(inp.upper()[0]==anskey[j]):
                    marks[i]+=10
anskey= ['A','B','B','C']
marks= [0 for i in range(5)]
students= list()
for i in range(5):
    name= input(f"Enter the name of student {i+1}: ")
    students.append(name)
calcScore(students, marks)
print("="*10)
print("Scores: ")
for i in range(5):
    print(f"{students[i]} got {marks[i]} marks.")
print("="*10)






