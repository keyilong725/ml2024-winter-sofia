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
