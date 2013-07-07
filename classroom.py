def average (grades) :
    return sum (grades) / len(grades)

def get_average (student) :
    weight_hw = average(student['homework']) * 0.10
    weight_qz = average(student['quizzes']) * 0.30
    weight_ts = average(student['tests']) * 0.60
    
    weighted_avg = weight_hw + weight_qz + weight_ts
    return weighted_avg

def get_class_average (student_list) :
    class_sum = 0
    
    for student in student_list :
        avg = get_average (student)
        class_sum += avg
        
    # calc the average of all students
    class_avg = class_sum / len(student_list)
    
    return class_avg

def get_letter_grade (score) :
    grade = "ERR"
    if score >= 90 : grade = 'A'
    elif score >= 80 : grade = 'B'
    elif score >= 70 : grade = 'C'
    elif score >= 60 : grade = 'D'
    else : grade = 'F'
    
    return grade

# data file with student info
lloyd = {
    "name": "Lloyd",
    "homework": [90.0, 97.0, 75.0, 92.0],
    "quizzes": [88.0, 40.0, 94.0],
    "tests": [75.0, 90.0]
}
alice = {
    "name": "Alice",
    "homework": [100.0, 92.0, 98.0, 100.0],
    "quizzes": [82.0, 83.0, 91.0],
    "tests": [89.0, 97.0]
}
tyler = {
    "name": "Tyler",
    "homework": [0.0, 87.0, 75.0, 22.0],
    "quizzes": [0.0, 75.0, 78.0],
    "tests": [100.0, 100.0]
}

# main
students = [lloyd, alice, tyler]
class_avg = get_class_average (students)
print class_avg
print get_letter_grade (class_avg)
