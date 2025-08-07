

# #Banking_appication
# import random
# class Bank:
#     total_user=[]   
#     def creat_new_bankaccount(self):
#         user_details={}
#         data=random.randint(100000000000,999999999999)
#         user_details['name']=input("Enter your name : ")
#         user_details['Mobile']=input('Enter your mobile number : ')
#         user_details['Aadhar_no']=input('Enter your aadhar no. :')
#         user_details['ifsc code ']='ANDB056535'
#         user_details['account_no']=data
#         n1=input('Select type od account saving/zero :').lower()
#         while True:
#             if n1=='saving':
#                 n2=int(input('Deposite 1000 rupees....'))
#                 if n2==1000:
#                     user_details['Balance']=n2
#                     break
#                 else:
#                     print("Deposite 1000 rupees.....")
#             elif n1=='zero':
#                 n3=int(input('Deposite 500 rupees...'))
#                 if n3==500:
#                     user_details['Balance']=n3
#                     break
#                 else:
#                     print("Deposite 500 rupees.....")
#         Bank.total_user.append(user_details)
#         print(Bank.total_user)
#         print('Your BankAccount Successfully Created')    
        
#     def deposite(self):
#         print('============Deposite Form =============')
#         name1=input('Enter your name :').lower()
#         account_num=int(input('Enter your Account number : '))
#         for user in Bank.total_user:
#             if name1==user['name'] and account_num==user['account_no']:
#                 deposite_money=int(input("Enter Deposite money : "))
#                 user['Balance']=user['Balance']+deposite_money
#                 print("Deposit successful!")
#                 print("Updated Balance:", user['Balance'])
#                 break
#             else:
#                 print('Deposite cancelld please check your name and password')
#     def withdrawl(self):
#         print('========== withdrawl Form =========')
#         name1=input('Enter your name :').lower()
#         account_num=int(input('Enter your Account number : '))
#         for user in Bank.total_user:
#             if name1==user['name'] and account_num==user['account_no']:
#                 withdrawl_money=int(input("Enter Withrawl money : "))
#                 user['Balance']=user['Balance']-withdrawl_money
#                 print("Withrawl successful!")
#                 print("Updated Balance:", user['Balance'])
#                 break
#             else:
#                 print('withdrawl cancelld please check your name and password')

# obj=Bank()
# obj.creat_new_bankaccount()
# obj.deposite()
# obj.withdrawl()





##
import random
class Bank:
    T_holders=[]
    def create_new_account(self):
        H_Details={}
        data=random.randint(100000000000,999999999999)
        H_Details["holder_name"]=input("Enter account holer name:")        
        H_Details["mobile_no"]=input("Enter mobile number:")
        H_Details["aadhar_no"]=input("Enter aadhar number:")
        H_Details["account_no"]=data
        H_Details["IFSC_no"]="IFSC506238"

        acc_type=input("Enter account type savings/zero:").lower()
        while True:
            if acc_type=="savings":
                d_amt=int(input("Deposite 1000 rupees:"))
                if d_amt>=1000:
                    H_Details["balance"]=d_amt
                    break
                else:
                    print("please deposite 1000 rupees.......")
            elif acc_type=="zero":
                de_amnt=int(input("deposite 500 rupees:"))
                if de_amnt>=500:
                    H_Details["balance"]=de_amnt
                    break
                else:
                    print(" Please deposite 500 rupees.....")

        Bank.T_holders.append(H_Details)
        print("Account created successfully")
        print(Bank.T_holders)

    def deposit(self):
        print("-----------------------------------------------------")
        name=input("Enter account holder name:")
        acc_no=int(input("Enter account number:"))
        deposite_amnt=int(input("Enter deposite number:"))
    
        for dep in Bank.T_holders:
            if dep ["holder_name"]==name and dep["account_no"]==acc_no:
                dep["balance"]=deposite_amnt+dep["balance"]
                print("Amount deposit successfully!")
                print("Updated Balance:",dep["balance"])
            else:
                print("Please enter correct details")

    def withdraw(self):
        print("-----------------------------------------------------")
        name=input("Enter account holder name:")
        a_no=int(input("Enter account number:"))
        withdraw_amnt=int(input("Enter withdraw amount:"))
        for user in Bank.T_holders:
            if user["holder_name"]==name and user["account_no"]==a_no:
                if user["balance"]>=withdraw_amnt:
                    user["balance"]=    user["balance"]-withdraw_amnt
                    print("withdrawl successful!")
                    print("Updated Balance:",user["balance"])
                else:
                    print("Insufficient balance")
            else:
                print("Please enter correct details")

    def checkbalence(self):
        print("-----------------------------------------------------")
        name=input("Enter account holder name:")
        acc_no=int(input("Enter account number:"))
        for x in Bank.T_holders:
            if x["holder_name"]==name and x["account_no"]==acc_no:
                print("Available Balance:",x["balance"])
            else:
                print("Please enter correct deatils")



obj=Bank()
obj.create_new_account()
obj.deposit() 
obj.withdraw()
obj.checkbalence()
