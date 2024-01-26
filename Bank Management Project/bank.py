from random import randint
from admin import Admin
from user import User
class Bank:
    def __init__(self,name,pass_key) -> None:
        self.Bank_name=name
        self.__TotalAmount=0
        self.__Total_Loan=0
        self.__Pass_Key=pass_key
        self.__Loan_Status=True
        self.__Users={}
        print(f"\n_________Welcome to {self.Bank_name}_________\n")

    @property
    def loan_status(self):
        return self.__Loan_Status
    
    @loan_status.setter
    def loan_status(self,status):
        self.__Loan_Status=status

    @property
    def Users_List(self):
        counter=0
        for key, user in self.__Users.items():
            if isinstance(user[0],Admin):
                continue
            else: 
                print(user[0])
                counter+=1
        if counter==0:
            print("\nNo user created account yet.")
    @property
    def Account_number(self)->str:
        return str(randint(1000,9999))+str(randint(1000,9999))+str(randint(10000,99999))

    @property
    def Balance(self):
        return self.__TotalAmount
    
    @Balance.setter
    def Balance(self,amount):
        self.__TotalAmount+=amount

    @property
    def Bank_Loan(self):
        return self.__Total_Loan

    @Bank_Loan.setter
    def Bank_Loan(self,amount):
        self.__Total_Loan+=amount

    def isvalid(self,ac_no,code)->bool:
        if code=='DU':
            return ac_no in self.__Users
        else:
            return ac_no in self.__Users and self.__Users[ac_no][3]=='User'
    def isOK(self,pass_key):
        return pass_key==self.__Pass_Key

    def request_to_transfer_amount(self,Info):
        self.__Users[Info[0]][0].Balance=Info

    def Creat_Account(self,designation)->User|Admin:
        name=input("Enter your name: ")
        email=input("Enter your email: ")
        pass_key=input("Enter a pass key: ")
        address=input("Enter your address: ")
        account_number=self.Account_number
        while account_number in self.__Users:
            account_number=self.Account_number
        if designation=='User':
            choice=input("Select account type:\n1) Savings\n2) Cuurent\n-->")
            account_type=lambda choice: 'Savings' if choice=='1'  else 'Cuurent' 
            user=User(self,name,email,account_number,pass_key,address,account_type(choice),designation)
            self.__Users[account_number]=(user,account_number,pass_key,designation)
            print(f"Welcome. to AC: {account_number}")
            return user
        else:
            admin=Admin(self,name,email,account_number,pass_key,address,designation)
            self.__Users[account_number]=(admin,account_number,pass_key,designation)
            print(f"Welcome. to AC: {account_number}")
            return admin
        
    def Login(self,designation)->User|Admin:
        counter=0
        while True:
            account_number=input("Enter your account number: ")
            password=input("Enter your password: ")
            if account_number in self.__Users and self.__Users[account_number][2]==password and self.__Users[account_number][3]==designation:
                print("Login successful")
                return self.__Users[account_number][0]
            elif counter<2:
                print("\nInvalid account number or password")
                counter+=1
            else:
                choice=input("\nOps! Haven't an account, Create one?\n1. Yes\n2. No\n-->")
                if choice=='1':
                    return self.Creat_Account(designation)
                else: continue


    def add_user(self,obj,account_number,pass_key,designation):
        if account_number in self.__Users:
            print("\nAccount number already esist")
        else:
            self.__Users[account_number]=(obj,account_number,pass_key,designation)

    def Delete_User(self,ac_no):
        del self.__Users[ac_no]

    def user_replica(self,user):
            while True:
                choice=input("\nWhat you wanna do?\n1. Deposit\n2. Withdraw\n3. Check Balance\n4. Check transaction history\n5. Take loan\n6. Pay Loan\n7. Transfer amount\n0. Logout\n-->")
                if choice=='1':
                    self.Balance=user.Deposit()
                elif choice=='2':
                    self.Balance=user.Withdraw()
                elif choice=='3':
                    user.Balance
                elif choice=='4':
                    user.Check_Transaction_History
                elif choice=='5':
                    user.Take_Loan()
                elif choice=='6':
                    user.Pay_Loan()
                elif choice=='7':
                    user.Transfer_Amount()
                elif choice=='0':
                    break

    def admin_replica(self,admin):
        while True:
            choice=input("\nWhat you wanna do?\n1. See user\n2. Delete account\n3. Available Balance\n4. Total Loan\n5. Change loan status\n0. Logout\n-->")
            if choice=='1':
                admin.See_Users
            elif choice=='2':
                admin.Delete_User()
            elif choice=='3':
                admin.Check_Balance
            elif choice=='4':
                admin.Check_Loaned_Amount
            elif choice=='5':
                admin.Loan_Status()
            elif choice=='0':
                break
