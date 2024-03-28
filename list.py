'''
Based on a Question
'''
class Student:
    def __init__(self, id, name, age, gpa):
        self.id=id
        self.name=name
        self.age=age
        self.gpa=gpa
        #next node
        self.next=None
class StudentDatabase:
    def __init__(self):
        self.head =None
    def addStudent(self, id, name, age, gpa):
        new_student=Student(id, name,age,gpa)
        if not self.head:
            self.head=new_student
        else: 
            current =self.head
            while current.next:
                current =current.next
            current.next = new_student
    def displayStudent(self):
        current=self.head
        while current:
            print(f"StudentID: {current.id} Name: {current.name} Age: {current.age} GPA: {current.gpa} ")
            current=current.next
student_db = StudentDatabase()
student_db.addStudent(100, 'Nyagaka', 19, 3.9)
student_db.addStudent(101, 'Vera', 21, 3.8)
student_db.addStudent(102, 'Moraa', 24, 4.0)
student_db.displayStudent()


