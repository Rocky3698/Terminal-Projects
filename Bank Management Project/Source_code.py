class User:
    def __init__(self,name,email,address,account_type,account_number,withdraw_limit) -> None:
        self.__Name=name
        self.__Email=email
        self.__Address=address
        self.__AcountType=account_type
        self.__Balance=0
        self.__Account_Number=account_number
        self.__Withdraw_Limit=withdraw_limit
        self.__Transaction_History={}
        self.__Loan_Count=0
        self.__Loan=0

    def Deposit(self)->int:
        amount=input('Enter deposit amount:')
        self.__Balance+=amount
        print(f"{amount} tk is added to account {self.__Account_Number} successfully.")
        if self.__Account_Number in self.__Transaction_History:
            self.__Transaction_History[self.__Account_Number].append(f"Deposit tk {amount} to account {self.__Account_Number}")
        else:
            self.__Transaction_History[self.__Account_Number]=(f"Deposit tk {amount} to account {self.__Account_Number}")
        return amount
    def Withdraw(self):
        amount=input('Enter withdraw amount:')
        if amount<=self.__Balance :
            if amount<=self.__Withdraw_Limit:
                self.__Balance-=amount
                print(f"Successfully withdraw {amount} tk.")
                if self.__Account_Number in self.__Transaction_History:
                    self.__Transaction_History[self.__Account_Number].append(f"Deposit tk {amount} to account {self.__Account_Number}")
                else:
                    self.__Transaction_History[self.__Account_Number]=(f"Deposit tk {amount} to account {self.__Account_Number}")
            else:
                print('\n|-_-| Bank is Bankrupt |-_-|\n')
        else:
            print('\n|-_-| Withdrawal amount exceeded |-_-|\n')

    def Check_Balance(self):
        print(f"Current balance is {self.__Balance} tk.\nCurrent loan is {self.__Loan} tk.")

    def Take_Loan(self):
        if(self.__Loan_Count<2):
            while True:
                amount=input('Enter loan amount:')
                if(amount<=self.__Withdraw_Limit):
                    self.__Loan+=amount
                    self.__Balance+=amount
                    print(f"Loan tk {amount} is added to your account successfully")
                    self.Histroy(amount,'Loan added',self.__Account_Number,'Bank')
                    break
                else:
                    print("\n|-_-| Sorry! Loan amount is too high |-_-|\n")
        else:
            print('|-_-| Loan limit exceeded |-_-|\nPay loan first.')
            self.Pay_Loan()

    def Pay_Loan(self):
        print(f"Enter amount to pay Loan tk {self.__Loan}.")
        amount=self.Deposit()
        self.__Loan-=amount
        print(f"Tk {self.Deposit()} is paid as load.\nCurrent loan {self.__Loan}.\nAccount Balance {self.__Balance}")
        self.Histroy(amount,'Loan paid','Bank',self.__Account_Number)

    def Transfer_Amount():
        pass

    def Histroy(self,amount,transaction_type,To,From):
        if self.__Account_Number in self.__Transaction_History:
            self.__Transaction_History[self.__Account_Number].append(f"{transaction_type} tk {amount} to {To} from {From}")
        else:
            self.__Transaction_History[self.__Account_Number]=(f"{transaction_type} tk {amount} to {To} from {From}")

    def Check_Transaction_History(self):
        print(self.__Transaction_History[self.__Account_Number])

class Bank:
    def __init__(self,name,email,address,account_type) -> None:
        self.__TotalAmount=0
        self.__Total_Loan=0
        self.__Users=[]
        self.Name="ABC BANK"
        self.__User=User(name,email,address,account_type,'0000 0000 0000'+str(self.__Users.__sizeof__()),self.__TotalAmount//5)
        self.__Users.append(self.__User)

    def Creat_Account():
        pass

    def Delete_User():
        pass

    def See_Users():
        pass

    def Check_Balance():
        pass

    def Check_Total_Loan_Amount():
        pass

    def Loan_Status():
        pass

