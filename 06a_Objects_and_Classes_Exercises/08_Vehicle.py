class Vehicle:

    def __init__(self, vehicle_type: str, model: str, price: int):
        self.vehicle_type = vehicle_type
        self.model = model
        self.price = price

        self.current_owner = None

    def buy(self, money: int, owner: str):
        if money >= self.price and self.current_owner is None:
            self.current_owner = owner
            return f"Successfully bought a {self.vehicle_type}. Change: {money - self.price:.2f}"
        elif money < self.price and self.current_owner is None:
            return "Sorry, not enough money"
        else:
            return "Car already sold"

    def sell(self):
        if self.current_owner is None:
            return "Vehicle has no owner"
        else:
            self.current_owner = None

    def __repr__(self):
        if self.current_owner is None:
            return f"{self.model} {self.vehicle_type} is on sale: {self.price}"
        else:
            return f"{self.model} {self.vehicle_type} is owned by: {self.current_owner}"


vehicle_type = "car"
model = "BMW"
price = 30000
vehicle = Vehicle(vehicle_type,model, price)
print(vehicle.buy(15000, "Peter"))
print(vehicle.buy(35000, "George"))
print(vehicle)
vehicle.sell()
print(vehicle)