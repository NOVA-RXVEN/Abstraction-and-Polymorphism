class Bangladesh:
    
    def capital(self):
        print("Dhaka is the Capital of Bangladesh.")
        
    def language(self):
        print("Bengali is the most widely spoken lanuage in Bangladesh.")
        
    def type(self):
        print("Bangladesh is a developing Country.")
        
class USA:
    
    def capital(self):
        print("Washington D.C. is the Capital of USA.")
        
    def language(self):
        print("English is the most widely spoken lanuage in USA.")
        
    def type(self):
        print("USA is a developing Country.")
        
objBan = Bangladesh()
objUSA = USA()

for country in (objBan, objUSA):
    country.capital()
    country.language()
    country.type()
    print()