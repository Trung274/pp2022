

class Student:
    def __init__(self, name, ID, m1, m2):
        self.name = name
        self.ID = ID
        self.m1 = m1
        self.m2 = m2
         
    def accept(self, Name, ID, marks1, marks2 ):
       
        ob = Student(Name, Rollno, marks1, marks2 )
        ls.append(ob)
  
    def display(self, ob):
            print("Name   : ", ob.name)
            print("ID : ", ob.ID)
            print("Marks1 : ", ob.m1)
            print("Marks2 : ", ob.m2)
            print("\n")    
  
    def search(self, rn):
        for i in range(ls.__len__()):
            if(ls[i].rollno == rn):
                return i       
  
ls =[]

obj = Student('', 0, 0, 0)

obj.accept("Trung", 1, 80, 100)
obj.accept("Nam", 2, 50, 90)
obj.accept("Linh", 100, 80)
         
print("\n")
print("\nList of Students\n")
for i in range(ls.__len__()):    
    obj.display(ls[i])
             



    