# 1)Student
# Создайте класс Student, конструктор которого имеет параметры name, lastname,
#
# department, year_of_entrance. Добавьте метод get_student_info, который
#
# возвращает имя, фамилию, год поступления и факультет в
#
# отформатированном виде: “Вася Иванов поступил в 2017 г. на факультет:
#
# Программирование.”

class Student:
    """Описание 'Student' """
    def __init__(self, name, lastname, year_of_entrance, department):
        """Свойства '' """

        self.name = name
        self.lastname = lastname
        self.year_of_entrance = year_of_entrance
        self.department =department

    def get_student_info(self):
        """Выводит сообщение в каком году поступил 'Student' """
        print("Student " + self.name + self.lastname +
              " Enrolled in " + str(self.year_of_entrance) + # чтобы введенное в обьекте числа считались как строки конвертируем их в "str"
              " years To the faculty " + self.department)

# Не забывайте пробелы между переданных в обьекте значениях чтобы на  выводе они не слепились
Student1 = Student("Adler ", "Franklin", 1995, "Programming")

    # """так мы выводим только "name" and "lastname" Students"""
    # print(Student1.name, Student1.lastname)  так мы выводим только "name" and "lastname" Students

Student1.get_student_info()








