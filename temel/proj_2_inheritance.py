class WebSite():
    "parent"
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def loginInfo(self):
        print(self.name + " " + self.surname)

class WebSite1(WebSite):
    "child"
    def __init__(self, name, surname, ids):
        super().__init__(name, surname)
        self.ids = ids
    
    def login(self):
        print(self.name + " " + self.surname + " " + self.ids)

class WebSite2(WebSite):
    def __init__(self, name, surname, email):
        super().__init__(name, surname)
        self.email = email

    def login(self):
        print(self.name + " " + self.surname + " " + self.email)

# p1 = WebSite("Hakan", "Akıncı")

p1 = WebSite("Hakan","Akıncı")
p2 = WebSite1("Ali","Can","123")
p3 = WebSite2("Caner","Fan","c@gmail.com")
p3.login()