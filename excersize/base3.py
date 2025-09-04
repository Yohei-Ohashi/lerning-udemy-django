grades = {
    "math": [85, 92, 78, 90, 88],
    "english": [88, 76, 95, 82, 91],
    "science": [91, 87, 84, 89, 93]
}

def get_rank(subject, student_number):
    score = grades[subject][student_number - 1]
    if score >= 90:
        print("A")
    elif score >= 80:
        print("B")
    elif score >= 70:
        print("C")
    else:
        print("D")
    return score

input_subject = input("科目名を入力してください（math/english/science）:")
input_student_number = int(input("学生番号を入力してください（1-5）:"))

get_rank(input_subject, input_student_number)