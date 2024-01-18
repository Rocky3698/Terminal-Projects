class Star_Cinema:
    hall_list=[]
    def entry_hall(self,obj):
        self.hall_list.append(obj)
class Hall(Star_Cinema):
    show_list=[]
    seats={}
    def __init__(self,rows,cols,hall_no) -> None:
        pass
        
    def entry_show(self,id,movie_name,time):
        self.show_list.append((id,movie_name,time))
    def book_seats(self,id,location):
        pass
    def view_show_list():
        pass
    def view_available_seats(self,id):
        pass
    


