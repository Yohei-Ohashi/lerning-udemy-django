"""演習問題5: 説明
以下の学生データを処理するプログラムを作成してください。
デコレータ、高階関数、lambda式、リスト内包表記を全て使用します。


実装要件

デコレータ: 実行時間測定機能(import timeでtime.time()を使用)
高階関数: 条件関数と変換関数を受け取るメソッド
lambda式: 条件判定と変換処理
リスト内包表記: データフィルタリング

数学80点以上の抽出: lambda式で条件判定し、「名前さん: 点数点」形式に変換
実行時間測定: デコレータで各処理の実行時間を自動計測して表示する


入力例

students = [
    {'name': '田中', 'score': 85, 'subject': 'math'},
    {'name': '佐藤', 'score': 92, 'subject': 'english'},
    {'name': '鈴木', 'score': 78, 'subject': 'math'},
    {'name': '高橋', 'score': 95, 'subject': 'science'},
    {'name': '渡辺', 'score': 88, 'subject': 'english'}
]
出力例

実行時間: 0.0001秒
数学80点以上: ['田中さん: 85点']
"""

import time


def start_end_time(func):
    def wrapper(*args, **kwargs):
        print("計測開始")
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        print("計測終了")
        print(f"実行時間: {end_time - start_time:.6f}秒")
        return result

    return wrapper


def filter_and_format(students, math_score_over_80, format_result):
    return [
        format_result(student) for student in students if math_score_over_80(student)
    ]


@start_end_time
def process_students(students):
    # ['田中さん: 85点']

    # 条件
    math_score_over_80 = (
        lambda student: student["subject"] == "math" and student["score"] >= 80
    )

    # フォーマット
    format_result = lambda student: f"{student['name']}さん: {student['score']}点"

    return filter_and_format(students, math_score_over_80, format_result)


def main():
    students = [
        {"name": "田中", "score": 85, "subject": "math"},
        {"name": "佐藤", "score": 92, "subject": "english"},
        {"name": "鈴木", "score": 78, "subject": "math"},
        {"name": "高橋", "score": 95, "subject": "science"},
        {"name": "渡辺", "score": 88, "subject": "english"},
    ]

    result = process_students(students)
    print(f"数学80点以上: {result}")


if __name__ == "__main__":
    main()
