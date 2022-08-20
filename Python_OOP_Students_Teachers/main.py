#Students and Lectors lists:

lecturers_list = []
students_list = []


class Student:
    def __init__(self, name, surname, gender):
        self.name = name
        self.surname = surname
        self.gender = gender
        self.finished_courses = []
        self.courses_in_progress = []
        self.grades = {}
        students_list.append(self)

    #Average grade
    def avg_grade(self):
        overall_grade = 0
        grades_count = 0
        if len(self.grades) == 0:
            return 0
        else:
            for grades in self.grades.values():
                if len(grades) > 0:
                    for grade in grades:
                        overall_grade += grade
                        grades_count += 1
            return overall_grade / grades_count

    #Adds completed course
    def add_courses(self, course_name):
        self.finished_courses.append(course_name)

    #Students rate Lectors
    def rate_lecturer(self, lecturer, course_name, grade):
        if isinstance(lecturer, Lecturer) and course_name in \
        self.courses_in_progress and course_name in \
        lecturer.courses_attached and 1 <= grade <= 10:
            lecturer.grades += [grade]
        else:
            return 'Wrong'

    #To print
    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Last Name: {self.surname}\n' \
               f'Average grade: {round(self.avg_grade(), 2)}\n' \
               f'Courses in progress: {", ".join(map(str, self.courses_in_progress))}\n' \
               f'Courses finished: {", ".join(map(str, self.finished_courses))}'

    #Comparing students using average grade. Returns boolean
    def __lt__(self, other):
        if isinstance(other, Student):
            return self.avg_grade() < other.avg_grade()
        else:
            return 'Wrong'


class Mentor:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        self.courses_attached = []


class Lecturer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.grades = []
        lecturers_list.append(self)

    #Lectors rate students
    def avg_grade(self):
        overall_grade = 0
        if len(self.grades) > 0:
            for grade in self.grades:
                overall_grade += grade
            return overall_grade / len(self.grades)
        else:
            return 0

    # Comparing lectors using average grade. Returns boolean
    def __lt__(self, other):
        if isinstance(other, Lecturer):
            return self.avg_grade() < other.avg_grade()
        else:
            return 'Wrong'

    #To print
    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Last Name: {self.surname}\n' \
               f'Average grade: {round(self.avg_grade(), 2)}'


class Reviewer(Mentor):
    def __init__(self, name, surname):
        super().__init__(name, surname)

    def __str__(self):
        return f'Name: {self.name}\n' \
               f'Last name: {self.surname}'

    def rate_hw(self, student, course, grade):
        if isinstance(student, Student) and course in \
        self.courses_attached and course in student.courses_in_progress:
            if course in student.grades:
                student.grades[course] += [grade]
            else:
                student.grades[course] = [grade]
        else:
            return 'Wrong'


def avg_grade_all_lecturers(lecturers_list, course_name):
    all_lecturers_avg_grade = 0
    lecturers_count = 0
    for lecturer in lecturers_list:
        if isinstance(lecturer, Lecturer) and course_name in \
        lecturer.courses_attached:
            all_lecturers_avg_grade += lecturer.avg_grade()
            lecturers_count += 1
    if lecturers_count == 0:
        return 'Wrong'
    return round(all_lecturers_avg_grade / lecturers_count, 2)


def avg_grade_all_students(students_list, course_name):
    all_students_avg_grade = 0
    students_count = 0
    for student in students_list:
        if isinstance(student, Student) and course_name in \
                student.courses_in_progress:
            all_students_avg_grade += student.avg_grade()
            students_count += 1
    if students_count == 0:
        return 'Wrong'
    return round(all_students_avg_grade / students_count, 2)


best_student = Student('Harry', 'Potter', 'male')
best_student.courses_in_progress += ['Python']
best_student.finished_courses += ['JavaScript']
best_student.add_courses('Git/GitHub')

worst_student = Student('Hermiona', 'Granger', 'female')
worst_student.courses_in_progress += ['Python']
worst_student.finished_courses += ['JavaScript']
worst_student.add_courses('Git/GitHub')

cool_reviewer = Reviewer("Lord", "Voldemort")
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['JavaScript']

cool_reviewer = Reviewer("Albus", "Dumbledore")
cool_reviewer.courses_attached += ['Python']
cool_reviewer.courses_attached += ['JavaScript']

cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'Python', 5)
cool_reviewer.rate_hw(best_student, 'JavaScript', 4)
cool_reviewer.rate_hw(best_student, 'JavaScript', 5)
cool_reviewer.rate_hw(best_student, 'JavaScript', 4)

cool_reviewer.rate_hw(worst_student, 'JavaScript', 5)
cool_reviewer.rate_hw(worst_student, 'JavaScript', 5)
cool_reviewer.rate_hw(worst_student, 'JavaScript', 5)
cool_reviewer.rate_hw(worst_student, 'Python', 4)
cool_reviewer.rate_hw(worst_student, 'Python', 5)
cool_reviewer.rate_hw(worst_student, 'Python', 3)

cool_lecturer = Lecturer('Ron', 'Weasley')
cool_lecturer.courses_attached += ['Python']
lecturers_list.append(cool_lecturer)

def_lecturer = Lecturer('Draco', 'Malfoy')
def_lecturer.courses_attached += ['Python']
lecturers_list.append(def_lecturer)

best_student.rate_lecturer(cool_lecturer, "Python", 10)
best_student.rate_lecturer(cool_lecturer, "Python", 8)
best_student.rate_lecturer(cool_lecturer, "Python", 9)

worst_student.rate_lecturer(def_lecturer, "Python", 6)
worst_student.rate_lecturer(def_lecturer, "Python", 7)
worst_student.rate_lecturer(def_lecturer, "Python", 8)

print('THE BEST LECTURER: ')
print(cool_lecturer)
print()
print('THE BEST REVIEWER: ')
print(cool_reviewer)
print()
print('THE BEST STUDENT: ')
print(best_student)
print()
print('BEST STUDENT vs WORST STUDENT: ')
print(best_student > worst_student)
print()
print('BEST LECTURER vs WORST LECTURER: ')
print(def_lecturer > cool_lecturer)
print()
print('AVERAGE LECTURERS GRADE: ')
print(avg_grade_all_lecturers(lecturers_list, 'Python'))
print()
print('AVERAGE STUDENTS GRADE: ')
print(avg_grade_all_students(students_list, 'Python'))