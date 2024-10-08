import datetime

# parent class
class VehicleRent:

    def __init__(self,stock):
        self.stock = stock
        self.now = 0

    def displayStock(self):
        """
            display stock
        """
        print("{} vecihle available to rent".format(self.stock))
        return self.stock

    def rentHourly(self, n):
        """
            rent hourly
        """
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicle available to rent.".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for hourly at {} hours.".format(n,self.now.hour))

            self.stock -= n
            
            return self.now
        
    def rentDaily(self, n):
        """
            rent daily
        """
        if n <= 0:
            print("Number should be positive")
            return None
        elif n > self.stock:
            print("Sorry, {} vehicle available to rent.".format(self.stock))
            return None
        else:
            self.now = datetime.datetime.now()
            print("Rented a {} vehicle for daily at {} hours.".format(n,self.now.hour))

            self.stock -= n
            
            return self.now

    def returnVehicle(self, request, brand):
        """
            return a bill
        """
        car_h_price = 10
        car_d_price = car_h_price*8/10*24
        bike_h_price = 5
        bike_d_price = bike_h_price*7/10*24

        rentalTime, rentalBasis, numOfVehicle = request
        bill = 0

        if brand == "car":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds/3600*car_h_price*numOfVehicle
                
                elif rentalBasis == 2: # daily
                    bill = rentalPeriod.seconds/(3600*24)*car_d_price*numOfVehicle

                if (2 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill*0.8

                print("Thank you for returning your whicle")
                print("Price: $ {}".format(bill))
                return bill
        
        elif brand == "bike":
            if rentalTime and rentalBasis and numOfVehicle:
                self.stock += numOfVehicle
                now = datetime.datetime.now()
                rentalPeriod = now - rentalTime

                if rentalBasis == 1: # hourly
                    bill = rentalPeriod.seconds/3600*bike_h_price*numOfVehicle
                
                elif rentalBasis == 2: # daily
                    bill = rentalPeriod.seconds/(3600*24)*bike_d_price*numOfVehicle

                if (4 <= numOfVehicle):
                    print("You have extra 20% discount")
                    bill = bill*0.8

                print("Thank you for returning your whicle")
                print("Price: $ {}".format(bill))
                return bill
         
        else:
            print("You do not rent a vehicle")
            return None

# child class 1
class CarRent(VehicleRent):

    global discount_rate
    discount_rate = 15

    def __init__(self,stock):
        super().__init__(stock)

    def discount(self, b):
        """
            discount
        """
        bill = b - (b*discount_rate)/100
        return bill

# child class 2
class BikeRent(VehicleRent):
    
    def __init__(self, stock):
        super().__init__(stock)


# customer
class Customer:
    
    def __init__(self): 
        pass

    def requestVehicle():
        """
            request vehicle
        """
        pass

    def returnVehicle():
        """
            return vehicle
        """
        pass