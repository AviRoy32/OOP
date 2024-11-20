class Student:
    def __init__(self,name,current_class,id):
        self.name=name
        self.current_class=current_class
        self.id=id

    def __repr__(self) -> str:
        return f'student name: {self.name},class: {self.current_class},id:{self.id}'

class Teacher:
    def __init__(self,name,subject,id):
        self.name=name
        self.subject=subject
        self.id=id

    def __repr__(self) -> str:
        return f'Teacher: {self.name},subject: {self.subject},id: {self.id}'
    
class school:
    def __init__(self,name):
        self.name=name
        self.teachers=[]
        self.students=[]

    def add_teacher(self,name,subject):
        id=len(self.teachers)+101
        teacher=Teacher(name,subject,id)
        self.teachers.append(teacher)

    def enroll(self,name,fee):
        if fee<6500:
            return 'not enough fee'
        else:
            id=len(self.students)+1
            student=Student(name,'C',id)
            self.students.append(student)
            return f'{name} is enrolled with id {id},extra money {fee-6500}'
        
    def __repr__(self) -> str:
        print('welcome to',self.name)
        print('--------OUR TEACHERS--------')
        for teacher in self.teachers:
            print(teacher)
        print('---------OUR STUDENTS--------')
        for student in self.students:
            print(student)
        return 'All done for now'
        

phitron=school('phitron')
phitron.enroll('Avi',5200)
phitron.enroll('Anik',7000)

phitron.add_teacher('Hridoy','Algo')
phitron.add_teacher('swapno','DS')
phitron.add_teacher('Dipta','DB')

print(phitron)