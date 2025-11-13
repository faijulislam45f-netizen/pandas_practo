class Student:
    def __init__(self, name, standard, subject,roll_no, marks):
        self.name = name
        self.standard = standard
        self.subject = subject
        self.roll_no = roll_no
        self.marks = marks

    def show(self):
        print(f" Name {self.name}, Stand is {self.standard}, Sub {self.subject}, Roll I'd {self.roll_no}, with {self.marks}%")
        
s1 = Student("Faijul Islam ", 12, "Physics", 20, 95, )
s2 = Student("Jainab Khan", 10, "Maths", 10, 70)
s3 = Student("Aisha Begum", 11, "Chemistry", 5, 85)
s4 = Student("Yusuf Ali", 12, "Science", 25, 90)

s1.show()
s2.show()
s3.show()
s4.show()