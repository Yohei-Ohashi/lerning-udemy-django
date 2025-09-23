from typing import Dict, Tuple


# 生徒の成績表を作成するクラス
class SchoolReport:

    # クラス変数
    school_name = "サプー中学校"

    def __init__(self, student_name: str, scores_dict: Dict[str, int]) -> None:
        """
        student_name: 生徒の名前
        scores_dict: 科目名と点数を格納した辞書
        例: {"数学": 80, "国語": 70, "英語": 60}
        """
        # 引数の検証
        if not student_name or not student_name.strip():
            raise ValueError("生徒名は空にできません")

        if not scores_dict:
            raise ValueError("成績データは空にできません")

        # 点数が0-100の範囲内かチェック
        for subject, score in scores_dict.items():
            if not isinstance(score, int):
                raise TypeError(f"{subject}の点数は整数で入力してください")
            if not 0 <= score <= 100:
                raise ValueError(f"{subject}の点数は0-100の範囲内で入力してください")

        self.student_name = student_name.strip()  # 前後の空白を削除
        self.scores_dict = scores_dict

    def calculate_average(self) -> Tuple[float, int]:
        count_subject = len(self.scores_dict)
        average = sum(self.scores_dict.values()) / count_subject
        return average, count_subject

    def display_score(self) -> None:
        print(f"{'*' * 10} {self.student_name} の成績 {'*' * 10}")
        for subject, score in self.scores_dict.items():
            print(f"{subject}: {score}点")

        average, count = self.calculate_average()
        print(f"{count}教科の平均点は{average:.2f}点です")
        print()


# テスト
def main():
    # 生徒データを辞書で管理
    student_data = {
        "田中 A": {"数学": 80, "国語": 70, "英語": 60},
        "鈴木 B": {"数学": 90, "国語": 85, "英語": 75},
        "斎藤 C": {"数学": 70, "国語": 80, "英語": 90},
    }

    print(f"学校名: {SchoolReport.school_name}")

    for student_name, scores_dict in student_data.items():
        try:
            sr = SchoolReport(student_name, scores_dict)
            sr.display_score()
        except (ValueError, TypeError) as e:
            print(f"エラー: {student_name} のデータで{e}")


if __name__ == "__main__":
    main()
