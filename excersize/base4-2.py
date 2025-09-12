def class_scores(class_name, students):
    print(f"{class_name}の成績処理を開始します")
    total = 0
    count = 0

    for student_name, score in students.items():
        total += score
        count += 1
        print(f"{student_name}: {score}")
    average = total / count if count else 0
    print(f"{class_name}の平均点: {average:.2f}点")
    return average


def school_scores(classes):
    school_total = 0
    class_count = 0
    for class_name, students in classes.items():
        average = class_scores(class_name, students)
        school_total += average
        class_count += 1
    school_average = school_total / class_count if class_count else 0
    print(f"学校全体の平均点: {school_average:.2f}点")


def main():
    classes = {
        "1年A組": {"佐藤": 85, "鈴木": 92, "高橋": 78},
        "1年B組": {"田中": 88, "渡辺": 76, "山本": 90, "中村": 85},
        "1年C組": {"伊藤": 80, "山田": 83},
    }

    school_scores(classes)


if __name__ == "__main__":
    main()
