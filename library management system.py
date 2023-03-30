d=["Harry potter","Rk Jain Engineering Mathematics","Engineering Physics","Engineering drawing","Adobe photoshop"]
def contents():
    for i in d:
        print("*",i)
contents()
class Library:
    def __init__(self,d,e):
        self.d=d
        self.e=e
    def widraw(self):
        if self.e in self.d:
            self.d.remove(self.e)
        else:
            print("Enter the correct book name")

    def submit(self):
        self.d.append(self.e)
    def display(self):
        print("list of books")
        for i in self.d:
            print("*",i,self.d.count(i))
    def add(self):
        self.d.append(self.e)
        print("Thank you for you giving new book to our library")

for i in range(10000000):
    print("----------------------------------")
    print("1.Withdraw")
    print("2.Return")
    print("3.Give a extra books")
    print("4.Display books")
    ch=int(input("Submit your choice: "))
    print("----------------------------------")
    if ch==1:
        e=input("Enter your book name to withdraw: ")
        ob=Library(d,e)
        ob.widraw()
    if ch==2:
        e=input("Enter your book name to return: ")
        ob=Library(d,e)
        ob.submit()
    if ch==3:
        e=input("Enter your new book name to add: ")
        ob=Library(d,e)
        ob.add()
    if ch==4:
        ob=Library(d,0)
        ob.display()