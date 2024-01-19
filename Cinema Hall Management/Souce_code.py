from datetime import date
class Star_Cinema:
    _hall_list=[]
    def entry_hall(self,obj):
        self._hall_list.append(obj)

class Hall(Star_Cinema):
    def __init__(self,rows,cols,hall_no) -> None:
        self.__rows=rows
        self.__cols=cols
        self.__hall_no=hall_no
        self.__show_list=[]
        self.__seats={}
        super().entry_hall(self)
    def is_valid(self,id)->bool:
        if id not in self.__seats:
            return True
        else:
            return False
    def entry_show(self,id,movie_name,time):
        self.__show_list.append((movie_name,id,time))
        self.__seats[id]=[[0 for _ in range(self.__rows)] for _ in range(self.__cols)]

    def book_seats(self,id,location):
        if self.is_valid(id)==True:
            print("\n\033[31mError! Invalid ID.\033[0m\n")
        else:
            if self.__seats[id][location[0]-1][location[1]-1]==1:
                print(location," \033[31mis already booked.\033[0m")
            else:
                self.__seats[id][location[0]-1][location[1]-1]=1
                print(f"\n\033[32m{location} is booked for you\033[0m\n")

    def view_show_list(self):
        print('-'*10)
        for tpl in self.__show_list:
            print(f"Movie Name: {tpl[0]}  Show ID: {tpl[1]}  Time: {tpl[2]}")
        print('-'*10,'\n')

    def view_available_seats(self,id):
        try:
            print("\nGreen seats are available for ",id,"\n")
            for lst in self.__seats[id]:
                for x in lst:
                    if x==0:
                        print(f"\033[32m{x}\033[0m",end=' ')
                    else:
                        print(f"\033[31m{x}\033[0m",end=' ')
                print()
                
        except:
            print("\n\033[31mError! Show ID is incorrect.\033[0m\n")
        print()
h=Hall(9,9,1)
h.entry_show('XXX','XYZ',f"{date.today()} 08:20 PM")
h.entry_show('XNZ','X',f"{date.today()} 06:00 PM")
while True:
    choice=input("1) View show list\n2) view avaiable seats\n3) Book ticket\n4) Add Show if Admin\n5) Exit\nEnter Choice: ")
    if choice=='1':
        h.view_show_list()
    elif choice=='2':
        id=input("Enter show ID: ")
        h.view_available_seats(id)
    elif choice=='3':
        id=input("Enter Show ID: ")
        row=int(input("Enter Row: "))
        col=int(input("Enter Column: "))
        if row>9 or col>9:
            print("\n\033[31mError! Invalid seat.\033[0m\n")
        else: h.book_seats(id,(row,col))
    elif choice=='4':
        id=input("Enter Show ID: ")
        if h.is_valid(id):
            movie_name=input("Enter Movie Name: ")
            time=input("Enter date time: ")
            h.entry_show(id,movie_name,time)
            print("\nShow is added successfully.")
        else:
            print("\n\033[31mERROR! Show ID is already exist\033[0m\n")
    else:
        break


