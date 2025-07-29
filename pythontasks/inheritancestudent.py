class Student:
    def __init__(self,firstname,lastname,email,studentid,adress,mobilenumber,subjectlearned,gpa,datejoined):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.studentid=studentid
        self.adress=adress
        self.mobilenumber=mobilenumber
        self.subjectlearned=subjectlearned
        self.gpa=gpa
        self.datejoined=datejoined
    def getfullname(self):
        print(self.firstname+''+self.lastname)
    def changeaddress(self,newaddress):
        self.adress=newaddress
        print("adreesses changed")
    def changenumber(self,newnumber):
        self.mobilenumber=newnumber
        print("mobile number changed")
    def getgpa(self):
        print("your gpa is :",self.gpa)