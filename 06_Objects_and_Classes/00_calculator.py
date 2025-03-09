class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return 'Error: Division by zero!'
        return a / b


class UserInterface:
    def __init__(self):
        self.calc = Calculator()  # Fixed the assignment

    def get_input(self):
        try:
            first_number = float(input('Enter first number: '))
            second_number = float(input('Enter second number: '))  # Fixed the prompt
            operator = input('Enter operator (+, -, *, /): ')  # Fixed the prompt
            return first_number, operator, second_number
        except ValueError:
            print("Invalid input. Please enter numerical values")
            return None, None, None

    def perform_calculation(self, first_number, operator, second_number):
        if operator == '+':
            return self.calc.add(first_number, second_number)
        elif operator == '-':
            return self.calc.subtract(first_number, second_number)
        elif operator == "*":
            return self.calc.multiply(first_number, second_number)
        elif operator == "/":
            return self.calc.divide(first_number, second_number)
        else:
            return "Error: Invalid operator!"

    def run(self):
        while True:
            first_number, operator, second_number = self.get_input()
            if first_number is None:
                continue
            result = self.perform_calculation(first_number, operator, second_number)  # Fixed the tuple unpacking
            print(f"Result: {result}")
            cont = input("Do you want to perform another calculation? (yes/no): ").strip().lower()

            if cont != "yes":
                print("Goodbye!")  # Fixed the typo
                break


if __name__ == '__main__':
    ui = UserInterface()
    ui.run()