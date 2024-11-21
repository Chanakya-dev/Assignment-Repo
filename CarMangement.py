class Car:
    def __init__(self, make, model, year, mileage, fuel_tank_capacity):
    
        self.make = make
        self.model = model
        self.year = year
        self.mileage = mileage
        self.fuel_tank_capacity = fuel_tank_capacity
        self.maintenance_tasks = []

    def add_mileage(self, miles):
        
        if miles > 0:
            self.mileage += miles
        else:
            print("Mileage must be a positive number.")

    def calculate_fuel_efficiency(self, kilometers_driven, litter_of_fuel):
        
        if litter_of_fuel > 0:
            return kilometers_driven / litter_of_fuel
        else:
            print("Litters of fuel must be greater than zero.")
            return None

    def display_car_details(self):
        
        print(f"\nCar Details:\nMake: {self.make}\nModel: {self.model}\nYear: {self.year}\nMileage: {self.mileage} miles")

    def display_maintenance_tasks(self):
        
        print("\nMaintenance Tasks:")
        if self.maintenance_tasks:
            for task in self.maintenance_tasks:
                print(f"- {task}")
        else:
            print("No maintenance tasks recorded.")


if __name__ == "__main__":
    
    make = input("Enter the car make: ")
    model = input("Enter the car model: ")
    year = int(input("Enter the car year: "))
    mileage = int(input("Enter the car mileage: "))
    fuel_tank_capacity = float(input("Enter the fuel tank capacity (litters): "))

    car = Car(make, model, year, mileage, fuel_tank_capacity)

    kilometers_driven = float(input("\nEnter the kilometers driven: "))
    litters_used = float(input("Enter the litters of fuel used: "))
    fuel_efficiency = car.calculate_fuel_efficiency(kilometers_driven, litters_used)


    while True:
        task = input(" type 'done' to finish : ")
        if task.lower() == "done":
            break
        car.add_maintenance_task(task)

    car.display_car_details()
    if fuel_efficiency:
        print(f"Fuel Efficiency: {fuel_efficiency:.2f} miles per litter")
    car.display_maintenance_tasks()

  
