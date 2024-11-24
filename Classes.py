# <!-- # Python Assignment: Car Management System

# ## Problem Statement

# Write a Python program to manage car details using **Classes** and **Objects**. The system should allow you to track car information like make, model, year, and mileage. It should also allow you to calculate the fuel efficiency of the car and perform maintenance tasks.

# ### Objectives
# 1. **Define a Car class**: This class should have:
#    - Attributes like `make`, `model`, `year`, `mileage`, and `fuel_tank_capacity`.
#    - Methods for:
#      - Adding mileage and fuel consumption.
#      - Calculating the fuel efficiency (miles per gallon).
#      - Displaying car details.

# 2. **Create a method for calculating fuel efficiency**: Fuel efficiency should be calculated based on:
#    - Formula: `fuel_efficiency = miles_driven / gallons_of_fuel`
#    - You should take input for the miles driven and gallons of fuel used.

# 3. **Maintenance tracking**: Create methods to track maintenance tasks (e.g., oil change, tire check). You should store a record of each maintenance task performed and display this list.

# 4. **Inheritance (Bonus)**: Implement a derived class `ElectricCar` that inherits from `Car` and adds additional functionality such as battery status and electric range.

# ### Input
# 1. **Car Details**: The make, model, year, and mileage of the car.
# 2. **Fuel Consumption**: The miles driven and gallons of fuel used.
# 3. **Maintenance Tasks**: The program should allow users to add maintenance tasks performed on the car.

# ### Output
# 1. The car's details, including:
#    - Make, model, year, mileage
# 2. Fuel efficiency (miles per gallon).
# 3. A list of maintenance tasks performed on the car.
# 4. For `ElectricCar`, display the battery status and electric range.

# ### Example Input
# ```python
# Enter the car make: Toyota
# Enter the car model: Camry
# Enter the car year: 2020
# Enter the car mileage: 15000

# Enter the miles driven: 400
# Enter the gallons of fuel used: 10

# Enter maintenance task: Oil change
# Enter maintenance task: Tire rotation
# ```
# ### Example Output
# - Car Details:
# - Make: Toyota
# - Model: Camry
# - Year: 2020
# - Mileage: 15000 miles

# - Fuel Efficiency: 40.00 miles per gallon

# Maintenance Tasks:
# - Oil change
# - Tire rotation

#  -->


class Myclass:
    def __init__(s, make, model, year, mileage, fuel_tank_capacity, miles_driven, gallons_of_fuel, maintenance_records):
        s.make = make
        s.model = model
        s.year = year
        s.mileage = mileage
        s.fuel_tank_capacity = fuel_tank_capacity
        s.miles_driven = miles_driven
        s.gallons_of_fuel = gallons_of_fuel
        s.maintenance_records = maintenance_records
        s.fuel_efficiency = s.calculate_fuel_efficiency()
        s.add_maintenance_task()  

    def calculate_fuel_efficiency(s):
        return s.miles_driven / s.gallons_of_fuel

    def add_maintenance_task(s):
        task1 = input("Enter the maintenance task1: ")
        task2 = input("Enter the maintenance task2: ")
        if task1:
            s.maintenance_records.append(task1)
            return task1
        if task2:
            s.maintenance_records.append(task2)
            return task2
        else:
            print("No maintenance task added")


make = input("Enter the make of the car: ")
model = input("Enter the model of the car: ")
year = input("Enter the year of the car: ")
mileage = int(input("Enter the mileage of the car: "))
fuel_tank_capacity = input("Enter the fuel capacity of the car: ")
print(" ")
miles_driven = int(input("Enter the miles driven by the car: "))
gallons_of_fuel = int(input("Enter the gallons: "))

maintenance_records = []

p1 = Myclass(make, model, year, mileage, fuel_tank_capacity, miles_driven, gallons_of_fuel, maintenance_records)

print("Car details: ")
print(f"Make: {p1.make}")
print(f"Model: {p1.model}")
print(f"Year: {p1.year}")
print(f"Mileage: {p1.mileage}")
print(f"Fuel Tank Capacity: {p1.fuel_tank_capacity}")
print(" ")
print(f"Fuel Efficiency: {p1.fuel_efficiency}")
print(" ")
print("Maintenance Tasks: ")
print(f"Task1: {p1.maintenance_records}")
print(f"Task2: {p1.maintenance_records}")
