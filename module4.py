# Ask the user for input N
N = int(input("Please enter a positive integer N: "))

# Create an empty list to store the N numbers user will provide
number_list = []

# Ask the user to provide N numbers
for i in range(N):
    number = int(input("Please enter number #" + str(i + 1) + ": "))
    number_list.append(number)

# Ask the user for input X
X = int(input("Please enter an integer X: "))

# Check if X is in the list of numbers
if X in number_list:
    index = number_list.index(X) + 1
    print(f"The index of number {X} is: {index}")
else:
    print("-1")
