"""TODO
1. 複数のクラスに所属する生徒の成績（点数）データをまとめ、 クラスごと、学校全体の平均点を計算して表示するプログラムを作成してください。
2. 各クラスには複数の生徒が在籍しており、「生徒名」と「得点」のペアで成績データが与えられています。
3. 各クラスごとに、生徒ごとの得点を出力し、最後にクラスの平均点を計算・表示してください。
4. 全クラスの処理が終わったら、学校全体の平均点を計算・表示してください。
    - クラスと継承を使用すること
    - setter, getterを用いること
"""


class GradeProcessor:
    """平均計算の共通機能"""

    def __init__(self):
        self._total = 0  # class_total_score や school_total_score に相当
        self._count = 0  # class_count や school_count に相当

    @property
    def total(self):
        return self._total

    @total.setter
    def total(self, value):
        self._total = value

    @property
    def count(self):
        return self._count

    @count.setter
    def count(self, value):
        self._count = value

    @property
    def average(self):
        return self._total / self._count if self._count > 0 else 0


class ClassProcessor(GradeProcessor):
    """クラスの成績処理(内側のループに相当)"""

    def __init__(self, name):
        super().__init__()
        self._name = name

    @property
    def name(self):
        return self._name

    def calculate_average(self, students):
        """生徒の成績を処理してクラス平均を返す"""
        print(f"{self.name}の成績処理を開始します")

        # 内側のループと同じ
        for student, score in students.items():
            print(f"{student}: {score}")
            self.total += score
            self.count += 1

        print(f"{self.name}の平均点: {self.average:.2f}点")
        return self.average


class SchoolProcessor(GradeProcessor):
    """学校全体の処理(外側のループに相当)"""

    def __init_(self):
        super().__init__()

    def calculate_average(self, classes):
        # 外側のループと同じ
        for class_name, students in classes.items():
            class_proc = ClassProcessor(class_name)
            class_avg = class_proc.calculate_average(students)

            self.total += class_avg  # school_total_score += class_avg
            self.count += 1  # school_count += 1

        print(f"学校全体の平均点: {self.average:.2f}点")


classes = {
    "1年A組": {"佐藤": 85, "鈴木": 92, "高橋": 78},
    "1年B組": {"田中": 88, "渡辺": 76, "山本": 90, "中村": 85},
    "1年C組": {"伊藤": 80, "山田": 83},
}

school_processor = SchoolProcessor()
school_processor.calculate_average(classes)


# school_total_score = 0
# school_count = 0

# for class_name, students in classes.items():
#     print(f"{class_name}の成績処理を開始します")

#     class_total_score  = 0
#     class_count = 0

#     for student, score in students.items():
#         print(f"{student}: {score}")
#         class_total_score += score
#         class_count += 1
#     class_avg = class_total_score / class_count
#     print(f"{class_name}の平均点: {class_avg:.2f}点")

#     school_total_score += class_avg
#     school_count += 1
# school_avg = school_total_score / school_count
# print(f"学校全体の平均点: {school_avg:.2f}点")
