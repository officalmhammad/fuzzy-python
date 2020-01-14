import time
print("**********LIBRARY Management System**********")
class Library:
    def __init__(self, booklist):
        self.booklist = booklist
        self.lendrecord = {}
    def addbook(self):
        book = input("Enter book name : ")
        self.booklist.append(book)
        print("Adding your book......")
        time.sleep(3)
        
        print("Book Added Succesfully")
    def lendbook(self):
        print("****BOOKS LIST****")
        print(Hammad.booklist)
        print("**Which book do you want to borrow? Write Name in Capital Letters: **")
        b = input()
        if b not in booklist:
            print("SORRY WE DON'T HAVE THIS BOOK!")
            print("WE WILL TRY TO ADD THIS BOOK SOON!")
        if b in booklist:
            print("Book is available, Tell us your name: ")
            name = input("Your Name here: ")
            self.booklist.remove(b)
            print("Just a moment...")
            time.sleep(3)
            self.lendrecord[b] = name 
            print(f"BOOK BORROWED SUCCESFULLY by {name}")
    def returnbook(self):
        print("**Which book do you want to Return? Write Name of Book in Capital Letters: **")
        b = input()
        self.booklist.append(b)
        del self.lendrecord[b]
        print("Wait....")
        time.sleep(3)
        print("BOOK RETURNED SUCCESFULLY")

if __name__ == "__main__":
     
    booklist = ["JAVA","PYTHON","C++","C","JS"]
    Hammad= Library(booklist)
    while True:
        print("What do you want?\nSelect an Option")
        print("1.Lend a Book \n2.Return a Book \n3.Add a Book\n4.Quit" )
        a = int(input())
        if a == 1:
            Hammad.lendbook()
        if a == 3:
            Hammad.addbook()
        if a== 2:
            Hammad.returnbook()
        if a == 4:
            print("Quiting ....")
            time.sleep(1.5)
            quit()