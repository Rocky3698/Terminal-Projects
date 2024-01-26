class User():
    def __init__(self,bank,name,email,account_number,pass_key,address,account_type,designation) -> None:
        self.__Name=name
        self.__Email=email
        self.__Pass_Key=pass_key
        self.__Address=address
        self.__AcountType=account_type
        self.__Account_Number=account_number
        self.__designation=designation
        self.__Transaction_History=[]
        self.__bank=bank
        self.__Balance=0
        self.__Loan=0
        self.__Loan_Count=0

    def Deposit(self)->int:
        amount=User.type_validity(input('Enter deposit amount:'))
        self.__Balance+=amount
        print(f"\n{amount} tk is added to account {self.__Account_Number} successfully.")
        self.Histroy(amount,'Deposit',self.__Account_Number,'Self')
        return amount
    
    def Withdraw(self)->int:
        amount=User.type_validity(input('Enter withdraw amount:'))
        if amount<=self.__Balance:
            if amount<=self.__bank.Balance:
                self.__Balance-=amount
                print(f"\nSuccessfully withdraw {amount} tk.")
                self.Histroy(amount,'Withdraw','Self',self.__Account_Number)
                return (-1*amount)
            else:
                print('\n|-_-| Bank is Bankrupt |-_-|\n')
        else:
            print('\n|-_-| Withdrawal amount exceeded |-_-|\n')

    def Take_Loan(self):
        if(self.__Loan_Count<2):
            if self.__bank.loan_status==False:
                print("\nSorry! Bank isn't offering any loan\n")
                return
            while True:
                amount=User.type_validity(input('Enter loan amount:'))
                if amount<=self.__bank.Balance and amount!=0:
                    self.__Loan+=amount
                    self.__Balance+=amount
                    self.__Loan_Count+=1
                    self.__bank.Bank_Loan=amount
                    self.__bank.Balance=(-1*amount)
                    print(f"\nLoan tk {amount} is added to your account successfully")
                    self.Histroy(amount,'Loan added',self.__Account_Number,'Bank')
                    break
                elif amount ==0:
                    print("\nAre you kinding?\n")
                else:
                    print("\n|-_-| Sorry! Loan amount is too high |-_-|\n")
        else:
            print('\n|-_-| Loan limit exceeded |-_-|\nPay loan first.\n')
            # self.Pay_Loan()

    def Pay_Loan(self):
        if self.__Loan==0:
            print("\nYou don't have any loan\n")
        else:
            amount=User.type_validity(input(f"Enter amount to pay Loan of tk {self.__Loan} :"))
            while True:
                if amount<=self.__Balance:
                    self.__Loan-=amount
                    self.__Balance-=amount
                    self.Histroy(amount,'Loan paid','Bank',self.__Account_Number)
                    print(f"Tk {amount} is paid as load.\nCurrent loan {self.__Loan}.\nAccount Balance {self.__Balance}")
                    self.__bank.Balance=amount
                    self.__bank.Bank_Loan=(-1*amount)
                    break
                else:
                    print(f"you don't have sufficient balance. Please deposite tk {amount-self.__Balance} ")
                    self.Deposit()

    def Transfer_Amount(self):
        while True:
            To=input('Enter account number: ')
            if self.__bank.isvalid(ac_no=To,code='TA')==False:
                print("User does not exist")
            elif To==self.__Account_Number:
                print("You can't transfer money to yourself")
            else:
                amount=User.type_validity(input('Enter transfer amount: '))
                while True:
                    if amount<=self.__Balance:
                        self.__Balance-=amount
                        self.__bank.request_to_transfer_amount((To,self.__Account_Number,amount))
                        self.Histroy(amount,'Transfered',To,self.__Account_Number)
                        print(f"{amount}tk transfered to account {To} successfully.")
                        # return (To,self.__Account_Number,amount)
                        break
                    elif self.__Loan_Count<2 and self.__bank.loan_status:
                        choice=input('\Insufficiant balance. Want to take Loan\n1) Yes\n2) No\n-->')
                        if choice=='1':
                            self.Take_Loan()
                        else:
                            print('\n|-_-| Transaction unsuccessful |-_-|\n')
                            break
                    else:
                        print('\n|-_-| Transaction unsuccessful |-_-|\n')
                        break
                break


    @property
    def Check_Transaction_History(self):
        for transaction in self.__Transaction_History:
            print(transaction)

    @property
    def Balance(self):
        print(f"Current balance is {self.__Balance} tk.\nCurrent loan is {self.__Loan} tk.")

    @classmethod
    def type_validity(cls,data):
        while True:
            try:
                return int(data)
            except ValueError:
                data=input("Please enter a valid amount: ")

    @Balance.setter
    def Balance(self,Info):
        self.__Balance+=Info[2]
        self.__bank.Balance=Info[2]
        self.Histroy(amount=Info[2],To=Info[0],From=Info[1],transaction_type='Bank tranfer')

    def Histroy(self,amount,transaction_type,To,From):
        if self.__Account_Number in self.__Transaction_History:
            self.__Transaction_History.append(f"{transaction_type} tk {amount} to {To} from {From}")
        else:
            self.__Transaction_History.append((f"{transaction_type} tk {amount} to {To} from {From}"))

    def __repr__(self) -> str:
        return f"Account No:{self.__Account_Number} | Balance: {self.__Balance} | Loan: {self.__Loan} | Name: {self.__Name} | Email: {self.__Email} | Address: {self.__Address} | Account_Type: {self.__AcountType} | Naming: {self.__designation}"
