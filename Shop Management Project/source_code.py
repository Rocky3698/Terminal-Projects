from time import sleep
from random import randint
class Product:
    products=[]
    def add_product(self) -> None:
        pass
    def remove_product(self) ->None:
        pass
    def see_products(self)-> None:
        pass
class Customer:
    customers=[]
    cart=[]
    Order_History=[]
    def user(self,**customer_info) -> None:
        self.customers.append(customer_info)
        with open("customers.txt","a") as file:
            s=f"{customer_info['user_name']}|{customer_info['password']}|{customer_info['name']}|{customer_info['mobile_number']}|{customer_info['address']}|{customer_info['employ']}"
            # S=s[:-1]
            file.write('\n'+s)
    def set_data(self):
        with open("customers.txt","r") as file:
            for line in file:
                Info=line.split('|')
                self.customers.append({'user_name':Info[0],'password':Info[1],'name':Info[2],'mobile_number':Info[3],'address':Info[4],"employ":Info[5][:-1]})
    def save_data(self):
        with open("customers.txt","w") as file:
            for data in self.customers:
                s=f"{data['user_name']}|{data['password']}|{data['name']}|{data['mobile_number']}|{data['address']}|{data['employ']}"
                file.write(s+'\n')

    def display_info(self):
        for dic in self.customers:
            for info,data in dic.items():
                print(info," : ",data,end="   ")
            print()
    def Order_History(self)->None:
        pass
    def menu(self):
        pass
    def is_valid(self,key,value)->bool:
        for user in self.customers:
            if user[key]==value:
                return True
        return False
    def is__valid(self,user_name,password):
        for user in self.customers:
            if user['user_name']==user_name and user['password']==password:
                return user['name'],True,int(user['employ'])
        return 'unknown',False,False
    def see_cart(self):
        pass
    def check_out_card():
        pass
    def add_to_cart():
        pass
    def add_to_wishlist():
        pass
    

class Sale:
    sales_history=[]
    def set_data(self)->None:
        with open("Sales_History.txt","r") as file:
            for line in file:
                Info=line.split('|')
                self.sales_history.append({'book_name':Info[0],'unit':Info[1],'price':Info[2],'customer':Info[3],'date':Info[4][:-1]})
    def Sales_History(self) -> None:
        total_money=0
        total_book=0
        for sell in self.sales_history:
            for key,val in sell.items():
                print(key," = ",val,end="  ")
            print()
            total_money+=int(sell['price'])
            total_book+=int(sell['unit'])
        print(f"Total book soled = {total_book}\nTotal money = {total_money}")
class Shop:
    employs=[]
    def Display(self,customer,admin) -> None:
        if admin:
            print(' '*53,"\033[31mAdmin panel:\033[0m")
            print(' '*66,"\033[34m0\033[0m) Home")
            print(' '*66,"\033[32m1\033[0m) Add employ")
            print(' '*66,"\033[32m2\033[0m) Add product")
            print(' '*66,"\033[32m3\033[0m) See product store")
            print(' '*66,"\033[32m4\033[0m) Sales history")
            print(' '*66,"\033[32m5\033[0m) Customers")
            print(' '*66,"\033[31m6\033[0m) Exit")
            print('\n'," "*61,"--> ",end="")
            s='(\033[34m0,\033[32m1,2,3,4,5,\033[31m6\033[0m)'
            while(True):
                choice=input()
                if choice=='0':
                    print()
                    self.Display(False,True)
                    return
                elif choice=='1':
                    Shop().Add_employ()
                elif choice=='2':
                    Product().add_product()
                elif choice=='3':
                    Product().see_products()
                elif choice=='4':
                    Sale().Sales_History()
                elif choice=='5':
                    Customer().display_info()
                else:
                    Design().Terminate()
                    break
                print('\n'," "*46,s,"--> ",end="")
                
        elif customer:
            print("you are a customer")
    def Add_employ(self)-> None:
        print()
    def Customer_List(self)->None:
        pass

class Design:
    def Heading(self):
        print('\n'," "*70,"\033[33mPAGE TURNERS\033[0m")
        print(" "*62,"\033[32mYour good friends are here\033[0m")
        print(" "*40,"-" * 75,'\n\n')  # Horizontal line

    def Login(self):
        while(True):
            print(' '*50,'Enter your user_name:',end=" ")
            user_name = input()
            print(' '*50,'Enter your password:',end=" ")
            pass_key = input()
            name,user,admin=Customer().is__valid(user_name,pass_key)
            # print(name,user,admin)
            if admin or user:
                print(' '*50,"\033[32mLogin successful\033[0m")
                sleep(1)
                print("Welcome Back,",f"\033[34m{name}\033[0m")
                Design().Heading()
                Shop().Display(user,admin)
                break
            else:
                print(' '*50,"\033[31mInvalid user_name or password\033[0m\n")
                print(' '*66,"1) Login again")
                print(' '*66,"2) exit")
                print('\n'," "*61,"--> ",end="")
                choice=input()
                if choice=='1':
                    self.Login()
                else:
                    Design().Terminate()
                    break

    def Registation(self):
        print(' '*50,'Enter your name:',end=" ")
        Name = input()
        print(' '*50,'Enter your phone number:',end=" ")
        Phn_number = input()
        if Customer().is_valid("mobile_number",Phn_number):
            print("You already have an account")
            return self.Login()
        print(' '*50,'Enter your address:',end=" ")
        Address = input()
        print(' '*50,'Enter a user_name:',end=" ")
        while True:
            user_name = input()
            if Customer().is_valid('user_name',user_name):
                print(' '*50,'\033[31mThis user name is already used\033[0m')
                print(' '*50,"Try from here:",f"{Name.split()[0]}{randint(100,999)}",',',f"{Name.split()[0]}{randint(100,999)}")
                print(' '*50,"\033[32mOr, creat new:\033[0m",end="")
            else:break
        print(' '*50,'Enter a password:',end=" ")
        pass_key = input()
        Customer().user(user_name=user_name,password=pass_key,name=Name,mobile_number=Phn_number,address=Address,employ='0')
        print(' '*50,"\033[32mYou have successfully registerd\033[0m")
        self.Heading()
        Shop().Display(True,False)
    def Terminate(self):
        Msg="\033[31mTerminating Program ..................\033[0m\n\033[34mTacking backups ..................\033[0m"
        for c in Msg:
            # if c=='\n':
            #     sleep(1)
            # else:
            #     sleep(0.1)
            print(c,end="")
        # sleep(1)
        print('\n\033[32mProgram Terminated Successfully.\033[0m')

    def Login_Panel(self):
        print(" "*43,"Please Eenter 1 | 2 :")
        print(" "*66,'1) Login')
        print(" "*66,'2) Registation')
        print(" "*66,'3) Exit')
        print('\n'," "*61,"--> ",end="")
        while True:
            LR=input()
            if LR=='1' or LR=='2' or LR=='3':
                break
            print(" "*60,"\033[31mYou need to login first.\033[0m",end="")
            print('\n'," "*61,"\033[34m--> \033[0m",end="")
        if LR=='1':
            self.Login()
        elif LR=='2':
            self.Registation()
        else: self.Terminate()
sale=Sale()
c=Customer()
c.set_data()
sale.set_data()
# for dic in c.customers:
#     print(dic)
_design = Design()
_design.Heading()
_design.Login_Panel()

# c.save_data()
# Terminate()
