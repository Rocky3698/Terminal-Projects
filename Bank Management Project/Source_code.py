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
        self.Histroy(amount,'Deposit',self.__Account_Number,'Self')
        return amount
    
    def Withdraw(self):
        amount=input('Enter withdraw amount:')
        if amount<=self.__Balance :
            if amount<=self.__Withdraw_Limit:
                self.__Balance-=amount
                print(f"Successfully withdraw {amount} tk.")
                self.Histroy(amount,'Withdraw','Self',self.__Account_Number)
            else:
                print('\n|-_-| Bank is Bankrupt |-_-|\n')
        else:
            print('\n|-_-| Withdrawal amount exceeded |-_-|\n')

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

    def Transfer_Amount(self):
        To=input('Enter account number: ')
        amount=int(input('Enter transfer amount: '))
        while True:
            if amount<=self.__Balance:
                self.__Balance-=amount
                Bank.request_to_transfer_amount(Bank(),amount,self.__Account_Number,To)
                self.Histroy(amount,'Transfered',To,self.__Account_Number)
                break
            elif self.__Loan_Count<2:
                choice=input('insufficiant balance. Want to take Loan\n1) Yes\n2) No')
                if choice=='1':
                    self.Take_Loan()
            else:
                print('|-_-| Transaction unsuccessful |-_-|')
                break

    def Histroy(self,amount,transaction_type,To,From):
        if self.__Account_Number in self.__Transaction_History:
            self.__Transaction_History[self.__Account_Number].append(f"{transaction_type} tk {amount} to {To} from {From}")
        else:
            self.__Transaction_History[self.__Account_Number]=(f"{transaction_type} tk {amount} to {To} from {From}")

    @property
    def Check_Transaction_History(self):
        print(self.__Transaction_History[self.__Account_Number])

    @property
    def Balance(self):
        print(f"Current balance is {self.__Balance} tk.\nCurrent loan is {self.__Loan} tk.")
    
    @property
    def __repr__(self) -> str:
        return f"Name: {self.__Name}  Email: {self.__Email}  Address: {self.__Address}  Account_Type: {self.__AcountType}  Account_Number: {self.__Account_Number}  Balance: {self.__Balance}  Loan: {self.__Loan}"
    
    @Balance.setter
    def Balance(self,amount):
        self.__Balance+=amount


class Bank:
    def __init__(self,name) -> None:
        self.Name=name
        self.__TotalAmount=0
        self.__Total_Loan=0
        self.__Users={}
        self.__Loan_Status=False
        # self.__User=User(name,email,address,account_type,'0000 0000 0000'+str(self.__Users.__sizeof__()),self.__TotalAmount//5)
        # self.__Users.append(self.__User)
    def is_valid(self)->bool:
        pass

    def request_to_transfer_amount(self,amount,From,To):
        self.__Users[To].Balance=amount
        

    def Creat_Account(self):
        name=input("Enter your name: ")
        email=input("Enter your email: ")
        address=input("Enter your address: ")
        choice=input("Select account type:\n1) Saving\n2) Cuurent")
        account_type=lambda choice: 'Saving' if choice=='1'  else 'Cuurent' 
        account_number='0000 0000 0000'+str(self.__Users.__sizeof__())
        self.__Users[account_number]=User(name,email,address,account_type(choice),account_number,self.__TotalAmount//5)

    def Delete_User(self):
        account_number=input("Enter account number: ")
        del self.__Users[account_number]
        print(f"Account {account_number} is deleted successfully")

    @property
    def See_Users():
        print(User().__repr__)

    @property
    def Check_Balance(self):
        print(f"Current bank balance is {self.__TotalAmount}")

    @property
    def Check_Total_Loan_Amount(self):
        print(f"Total loan given tk {self.__Total_Loan}")

    def Loan_Status(self):
        if self.__Loan_Status:
            choice= input("Loan feature is ON\n1) Turn OFF\n2) Menu")
            if choice=='1':
                self.__Loan_Status=False
            else: return None
        else:
            choice= input("Loan feature is OFF\n1) Turn ON\n2) Menu")
            if choice=='1':
                self.__Loan_Status=True
            else: return None

        

