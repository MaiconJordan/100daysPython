student_scores = {
    "Harry" : 81,
    "Rin": 78,
    "Hermano": 99,
    "Draco": 74,
    "Neville": 10
}


student_grades = {}

for note in student_scores:    
    if student_scores[note] >= 91:
        student_grades[note] = "Passed"
print(student_grades)
    
