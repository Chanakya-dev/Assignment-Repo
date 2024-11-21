array=[11,22,33,44,55,66]
print(array[0])
print(array[5])

for x in array:
    print(x)

array = [12,23,34,45,56,67,78]
print("Original Array:", array)

reversed_array = array[::-1]
print("Reversed Array:", reversed_array)

total = sum(array)
print("Sum of elements:", total)

array = [45,75,98,78,41,62,54,95]
largest = max(array)
smallest = min(array)
print("Largest Element:", largest)
print("Smallest Element:", smallest)

array.insert(1,20)
print(array)

array.append(0.5)
print(array)

array1=[1, 2, 3, 4, 5]
array1.remove(4)
print(array1)

array1.pop(1)
print(array1)

array1.extend(array)
print(array1)

number = 10
for i in range(1, 11):
    print(f"{number} x {i} = {number * i}")
