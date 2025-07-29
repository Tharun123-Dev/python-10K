class Faculty:
    def __init__(self,firstname,lastname,email,facultyid,adress,mobilenumber,subjectteaching,salary,datejoined):
        self.firstname=firstname
        self.lastname=lastname
        self.email=email
        self.facultyid=facultyid
        self.adress=adress
        self.mobilenumber=mobilenumber
        self.subjectteaching=subjectteaching
        self.salary=salary
        self.datejoined=datejoined
    def getfullname(self):
        print(self.firstname+''+self.lastname)
    def changeaddress(self,newaddress):
        self.adress=newaddress
        print("adreesses changed")
    def changenumber(self,newnumber):
        self.mobilenumber=newnumber
        print("mobile number changed")
    def getsalary(self):
        print("your salary is :",self.salary)