"""
Person klassini yarating, unda name va age atributlari bo‘lsin.
Professor va Student klasslarini Persondan meros qilib oling.
Professor uchun teach metodi, Student uchun study metodi bo‘lsin.
Universitetning kurslar va odamlarni boshqarish tizimini yaratib ko‘ring.
"""

students : list['Student']  = []
professors : list['Professor'] = []
subjects : list['Subject']= []


class Person:
    def __init__(self ,id , name , age):
        self.id = id
        self.name = name
        self.age = age

    def add(self):
        pass

    def __repr__(self):
        return f"{self.__class__.__name__}(id={self.id},name={self.name},age={self.age})"


class Professor(Person):
    def __init__(self ,
                 id = None ,
                 name = None ,
                 age = None ,
                 salary= None ,
                 subject = None):
        super().__init__(id,name, age)
        self.salary = salary
        self.subject = subject
    def teach(self):
        return self.subject

    def add(self):
        self.id = professors[-1].id + 1 if professors else 1
        professors.append(self)

    def __repr__(self):
        return super().__repr__()[:-1] + f",salary={self.salary},subject={self.subject.name})"


class Student(Person):
    def __init__(self ,
                 id= None,
                 name = None,
                 age = None,
                 course = None ,
                 faculty = None):
        super().__init__(id,name, age)
        self.course = course
        self.faculty = faculty

    def study(self):
        return f"Course : {self.course}\nFaculty : {self.faculty}"

    def add(self):
        self.id = students[-1].id + 1 if students else 1
        students.append(self)



class Subject:
    def __init__(self ,
                 id = None,
                 name = None):
        self.id = id
        self.name = name

    def add(self):
        self.id = subjects[-1].id + 1 if subjects else 1
        subjects.append(self)

    def __repr__(self):
        return f"Subject(id={self.id},name={self.name})"

#
#
s1 = Subject(name="Matematika")
s1.add()
print(subjects)
p1 = Professor(name="Vali" , age=40 ,salary=1000,subject=s1)
p1.add()
print(professors)



