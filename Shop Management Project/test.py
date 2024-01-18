# class cst:
#     arr=[]
#     def set_data(self):
#         with open("/Users/rabbi/OneDrive/Desktop/Rocky/Bootcamp/Shop Management Project/customers.txt","r") as file:
#             Info=file.readline().split('|')
#             print(Info,type(Info))
#         # file = open(, "r")
#         # for line in file:
#         #     print(line)
#         # file.close()
# ob=cst()
# ob.set_data()
# dic={"name":"Rocky","Age":"22","Gender":"Male"}
# dic['job']='student'
# print(dic)
# with open("/Users/rabbi/OneDrive/Desktop/Rocky/Bootcamp/Shop Management Project/customers.txt","r") as file:
#     # Info=file.readline().split('|')
#     for line in file:
#         print(line,type(line),end="")
# print(type(Info))
# print(Info)
# c=[{'user_name': 'Rocky20809', 'password': 'shahin567&*-', 'name': 'Rocky', 'mobile_number': '01639066718', 'address': 'Gopinathpur\n'},
# {'user_name': 'Shain20809', 'password': 'rocky567&*-', 'name': 'Shahin', 'mobile_number': '01858351717', 'address': 'Darul Aman\n'},
# {'user_name': 'Imtiaz', 'password': 'rocky4r', 'name': 'dfdl', 'mobile_number': '345454954', 'address': 'fdfld\n'},
# {'user_name': 'fdkfldlfk', 'password': 'kfdlfk', 'name': 'repwro', 'mobile_number': '33090493', 'address': 'dfkdfk\n'},
# {'user_name': 'dkfjdfjd', 'password': 'eoweirr', 'name': 'rkeork', 'mobile_number': '3049349', 'address': 'fdlfd'}]
# with open("/Users/rabbi/OneDrive/Desktop/Rocky/Bootcamp/Shop Management Project/customers.txt","a") as file:
#     for data in c:
#         s=f"{data["user_name"]}|{data["password"]}|{data["name"]}|{data["mobile_number"]}|{data["address"]}"
#         S=s[:-1]
#         file.write('\n'+S)


# import datetime
# print(datetime.date.today())