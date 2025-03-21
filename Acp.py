class Porsche:
    
    def Model(self):
        print("\033[1mModel: Porsche 911 GT3 \033[0m")
        
    def Top_Speed(self):
        print("Top Speed: 317 km/h")
        
    def Price(self):
        print("Price: $170,000")
    
    def Horse_Power(self):
        print("Horse Power: 502")
    
    def Milage(self):
        print("Milage: 15-20")
        
class Lamorghini:
    
    def Model(self):
        print("\033[1mModel: Lamborghini Aventador\033[0m")
        
    def Top_Speed(self):
        print("Top Speed: 354 km/h")
        
    def Price(self):
        print("Price: $400,000")
    
    def Horse_Power(self):
        print("Horse Power: 730")
    
    def Milage(self):
        print("Milage: 10-16")

class Ferrari:
    
    def Model(self):
        print("\033[1mModel: LaFerrari\033[0m")
        
    def Top_Speed(self):
        print("Top Speed: 350 km/h")
        
    def Price(self):
        print("Price: $1.5 million")
    
    def Horse_Power(self):
        print("Horse Power: 950")
    
    def Milage(self):
        print("Milage: 12-19")        

class koenigsegg:
    
    def Model(self):
        print("\033[1mModel: Koenigsegg Jesko\033[0m")
        
    def Top_Speed(self):
        print("Top Speed: 483 km/h")
        
    def Price(self):
        print("Price: $2.8 million")
    
    def Horse_Power(self):
        print("Horse Power: 1600")
    
    def Milage(self):
        print("Milage: 10-15")

class Pagani:
    
    def Model(self):
        print("\033[1mModel: Pagani Huayra\033[0m")
        
    def Top_Speed(self):
        print("Top Speed: 372 km/h")
        
    def Price(self):
        print("Price: $2.6 million")
    
    def Horse_Power(self):
        print("Horse Power:  730 horsepower")
    
    def Milage(self):
        print("Milage: 14-17")

objPorsche = Porsche()
objLambo = Lamorghini()
objFerrari = Ferrari()
objKoenig = koenigsegg()
objPagani = Pagani()

for car in (objPorsche, objLambo, objFerrari, objKoenig, objPagani):
    car.Model()
    print()
    car.Top_Speed()
    car.Price()
    car.Horse_Power()
    car.Milage()
    print()
    print()