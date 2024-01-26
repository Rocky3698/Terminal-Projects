from user import User
from admin import Admin
from bank import Bank

def main():
    bank=Bank("ABC BANK","****")
    # user=User(bank,'shahin','shahin@gmail.com','1234567891011','****','Dhaka','Savings','User')
    # _User=User(bank,'shahin','shahin@gmail.com','1234567891013','****','Dhaka','Savings','User')
    # admin=Admin(bank,'Rocky','rocky@gmail.com','1234567891012','****','Dhaka','Admin')
    # bank.add_user(user,'1234567891011','****','User')
    # bank.add_user(admin,'1234567891012','****','Admin')
    # bank.add_user(_User,'1234567891013','****','User')

    # user.Balance='1234567891011','1234567891011',100
    # user.Balance
    # # print(user)
    # print(isinstance(_User,User))

    while True:
        choice=input("1. User   |   2. Admin   |    0. Exit\n-->")
        if choice=='1':
            Choice=input("1. Login\n2. Signup\n-->")
            if Choice=='1':
                user=bank.Login('User')
                bank.user_replica(user)
                pass
            elif Choice=='2':
                user=bank.Creat_Account('User')
                bank.user_replica(user)
            else: continue
        elif choice=='2':
            pass_key=input("Enter pass key: ")
            if bank.isOK(pass_key):
                Choice=input("1. Login\n2. Signup\n-->")
                if Choice=='1':
                    bank.admin_replica(bank.Login('Admin'))
                elif Choice=='2':
                    bank.admin_replica(bank.Creat_Account('Admin'))
                else: continue
            else:
                print("Invalid pass key.")
        else: break


if __name__=='__main__':
    main()


