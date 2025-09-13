def class_scores(class_name, students):
    """クラス平均点を計算します

    引数:
        class_name: クラス名
        students: 学生名と点数の辞書

    戻り値:
        クラス平均点
    """
    print(f"{class_name}の成績処理を開始します")
    total = 0
    count = 0
    
    for student_name, score in students.items():
        yield {
            "type": "student",
            "student_name": student_name,
            "score": score,
        }
        total += score
        count += 1
    average = total / count if count else 0
    return {
        "type": "class_average",
        "class_name": class_name,
        "average": average,
    }


def school_scores(classes):
    """学校全体の平均点を計算します

    引数:
        classes: クラス名と学生名、点数の辞書

    戻り値:
        学校全体の平均点
    """
    school_total = 0
    class_count = 0
    for class_name, students in classes.items():
        average = yield from class_scores(class_name, students)
        yield average
        school_total += average["average"]
        class_count += 1
    school_average = school_total / class_count if class_count else 0
    yield {
        "type": "school_average",
        "average": school_average,
    }


def main():
    classes = {
        "1年A組": {"佐藤": 85, "鈴木": 92, "高橋": 78},
        "1年B組": {"田中": 88, "渡辺": 76, "山本": 90, "中村": 85},
        "1年C組": {"伊藤": 80, "山田": 83},
    }

    gen = school_scores(classes)
    for result in gen:
        if result["type"] == "student":
            print(f"{result['student_name']}: {result['score']}")
        elif result["type"] == "class_average":
            print(f"{result['class_name']}の平均点: {result['average']:.2f}点")
        elif result["type"] == "school_average":
            print(f"学校全体の平均点: {result['average']:.2f}点")


if __name__ == "__main__":
    main()
