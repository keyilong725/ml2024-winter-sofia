class Number_Search:
    def __init__(self):
        self.numbers = []

    def insert_number(self, number):
        self.numbers.append(number)

    def find_index(self, x):
        if x in self.numbers:
            return self.numbers.index(x) + 1  
        else:
            return -1

def main():
    numbers = Number_Search()

    # Get the number of inputs
    n = int(input("Please enter a positive integer N: "))

    # Obtain the numbers
    for i in range(n):
        num = int(input("Please enter number #" + str(i + 1) + ": "))
        numbers.insert_number(num)

    # Get input X and find its index
    x = int(input("Enter an interger X: "))
    index = numbers.find_index(x)
    print("Index of input X is: ", index)

# Call the function
if __name__ == "__main__":
    main()
    
