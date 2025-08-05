import random
class Bank:
    def Create_New_Acc(self):
          U_details={}
          data=random.randint(100000000000,999999999999)
          U_details["Name"]=input("enter a name : ")
          U_details["mobile"]=input("enter a number: ")
          U_details["adhaar"]=input("enter a  aadhar number: ")
          U_details["IFSC"]="IFSCNANI123"
          U_details["mobile"]=data
    n1=input("select type of Account Savings/Zero...")
    