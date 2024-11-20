# Python Assignment: Car Management System

## Problem Statement

Write a Python program to manage car details using **Classes** and **Objects**. The system should allow you to track car information like make, model, year, and mileage. It should also allow you to calculate the fuel efficiency of the car and perform maintenance tasks.

### Objectives
1. **Define a Car class**: This class should have:
   - Attributes like `make`, `model`, `year`, `mileage`, and `fuel_tank_capacity`.
   - Methods for:
     - Adding mileage and fuel consumption.
     - Calculating the fuel efficiency (miles per gallon).
     - Displaying car details.

2. **Create a method for calculating fuel efficiency**: Fuel efficiency should be calculated based on:
   - Formula: `fuel_efficiency = miles_driven / gallons_of_fuel`
   - You should take input for the miles driven and gallons of fuel used.

3. **Maintenance tracking**: Create methods to track maintenance tasks (e.g., oil change, tire check). You should store a record of each maintenance task performed and display this list.

4. **Inheritance (Bonus)**: Implement a derived class `ElectricCar` that inherits from `Car` and adds additional functionality such as battery status and electric range.

### Input
1. **Car Details**: The make, model, year, and mileage of the car.
2. **Fuel Consumption**: The miles driven and gallons of fuel used.
3. **Maintenance Tasks**: The program should allow users to add maintenance tasks performed on the car.

### Output
1. The car's details, including:
   - Make, model, year, mileage
2. Fuel efficiency (miles per gallon).
3. A list of maintenance tasks performed on the car.
4. For `ElectricCar`, display the battery status and electric range.

### Example Input
```python
Enter the car make: Toyota
Enter the car model: Camry
Enter the car year: 2020
Enter the car mileage: 15000

Enter the miles driven: 400
Enter the gallons of fuel used: 10

Enter maintenance task: Oil change
Enter maintenance task: Tire rotation
```
### Example Output
- Car Details:
- Make: Toyota
- Model: Camry
- Year: 2020
- Mileage: 15000 miles

- Fuel Efficiency: 40.00 miles per gallon

Maintenance Tasks:
- Oil change
- Tire rotation
