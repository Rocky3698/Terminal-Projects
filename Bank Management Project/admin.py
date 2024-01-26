class Admin:
    def __init__(self,bank,name,email,account_number,pass_key,address,designation) -> None:
        self.__Name=name
        self.__Email=email
        self.__Account_Number=account_number
        self.__Pass_Key=pass_key
        self.__Address=address
        self.__Designation=designation
        self.__bank=bank

    def Delete_User(self):
        account_number=input("Enter account number: ")
        if self.__bank.isvalid(ac_no=account_number,code='DU'):
            self.__bank.Delete_User(account_number)
            print(f"Account {account_number} is deleted successfully")
        else:
            print("|-_-| Invalid account number |-_-|")

    @property
    def See_Users(self):
        self.__bank.Users_List

    @property
    def Check_Balance(self):
        print(f"Current bank balance is {self.__bank.Balance}")

    @property
    def Check_Loaned_Amount(self):
        print(f"Total loan given tk {self.__bank.Bank_Loan}")

    def Loan_Status(self):
        if self.__bank.loan_status:
            choice= input("Loan feature is ON\n1) Turn OFF\n2) Menu\n-->")
            if choice=='1':
                self.__bank.loan_status=False
                print("Bank stoped offering loan")
            else: return None
        else:
            choice= input("Loan feature is OFF\n1) Turn ON\n2) Menu\n-->")
            if choice=='1':
                self.__bank.loan_status=True
                print("Bank is offering loan")
            else: return None
