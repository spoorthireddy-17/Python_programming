n = int(input("Enter number of elements: "))
numbers = []
for i in range(n):
    num = int(input(f"Enter element {i+1}: "))
    numbers.append(num)
if len(set(numbers)) < 2:
    print("No second largest element (not enough unique numbers)")
else:
    second_largest = sorted(set(numbers), reverse=True)[1]
    print("Second largest element:", second_largest)
