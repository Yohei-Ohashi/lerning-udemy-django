grades = {
    "math": [85, 92, 78, 90, 88],
    "english": [88, 76, 95, 82, 91],
    "science": [91, 87, 84, 89, 93],
}


class ScoreError(Exception):
    pass


def get_rank(subject, student_number):
    # 科目の存在確認
    if subject not in grades:
        raise KeyError(f"指定した科目 '{subject}' が存在しません")

    # 学生番号の範囲確認
    if not 1 <= student_number <= len(grades[subject]):
        raise ScoreError(f"学生番号 '{student_number}' が存在しません")

    # 成績判定
    score = grades[subject][student_number - 1]
    if not 0 <= score <= 100:
        raise ValueError("成績が0-100の範囲外です")
    if score >= 90:
        grade = "A"
    elif score >= 80:
        grade = "B"
    elif score >= 70:
        grade = "C"
    elif score >= 60:
        grade = "D"
    else:
        grade = "F"
    print(f"評価: {grade}")


def main():
    print("=== 成績管理システム ===")

    try:
        input_subject = input("科目名を入力してください（math/english/science）:")
        input_student_number = int(input("学生番号を入力してください（1-5）:"))

        get_rank(input_subject, input_student_number)
    except KeyError as e:
        print(f"{type(e).__name__}: {e}")
    except ValueError as e:
        print(f"{type(e).__name__}: 入力が正しくありません")
    except IndexError as e:
        print(f"{type(e).__name__}: {e}")
    except ScoreError as e:
        print(f"{type(e).__name__}: {e}")
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
        print("予期せぬエラーが発生しました")
    else:
        print("正常に処理が完了しました")
    finally:
        print("=== 成績管理システムを終了します ===")


if __name__ == "__main__":
    main()
