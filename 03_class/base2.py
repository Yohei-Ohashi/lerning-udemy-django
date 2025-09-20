class Student:
    # クラス変数
    school_name = "ABC学園"
    
    def display_info(self):
        print(f"{self.school_name}: {self.name}")
    
    # インスタンスメソッド
    def set_school_name(self, name):
        self.school_name = name
    
    def set_name(self, name):
        self.name = name

student_1 = Student()
student_2 = Student()

print(id(student_1), id(student_2))
print(student_1.school_name, student_2.school_name)
print(id(student_1.school_name), id(student_2.school_name))

# クラス変数
Student.school_name = "DEF学園"
print(student_1.school_name, student_2.school_name)
print(id(student_1.school_name), id(student_2.school_name))

# student_1だけ変更
student_1.set_school_name("GHI学園")
print(student_1.school_name, student_2.school_name)
print(id(student_1.school_name), id(student_2.school_name))

student_1 = Student()
student_2 = Student()
student_1.set_name("Taro")
student_2.set_name("Jiro")
student_1.display_info()
student_2.display_info()