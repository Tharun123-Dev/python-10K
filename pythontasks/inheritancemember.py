class Member:
    def __init__(self,firstname,lastname,email,memberid,adress,mobilenumber,datejoined):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.memberid=memberid
        self.adress=adress
        self.mobilenumber=mobilenumber
        self.datejoined=datejoined
    def getfullname(self):
        print(self.firstname+''+self.lastname)
    def changeaddress(self,newaddress):
        self.adress=newaddress
        print("adreesses changed")
    def changenumber(self,newnumber):
        self.mobilenumber=newnumber
        print("mobile number changed")

class Faculty(Member):
    def __init__(self,firstname,lastname,email,memberid,adress,mobilenumber,subjectteaching,salary,datejoined):
       
        self.subjectteaching=subjectteaching
        self.salary=salary
    
        Member.__init__(self,firstname,lastname,email,memberid,adress,mobilenumber,datejoined)
       
    def getsalary(self):
        print("your salary is :",self.salary)

class Student(Member):
    def __init__(self,firstname,lastname,email,memberid,adress,mobilenumber,subjectlearned,gpa,datejoined):
       
        self.subjectlearned=subjectlearned
        self.gpa=gpa
        Member.__init__(self,firstname,lastname,email,memberid,adress,mobilenumber,datejoined)
     
    def getgpa(self):
        print("your gpa is :",self.gpa)

obj=Student("nani","tharun","email","123","hyd","344","eng","10","23/23")
print(obj.firstname)
print(obj.memberid)