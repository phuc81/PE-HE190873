class Employee:
    def __init__(self, name, salary, age):
        self.name = name
        self.salary = salary
        self.age = age

def input_employee():
    name = input("Enter name: ")
    salary = float(input("Enter salary: "))
    age = int(input("Enter age: "))
    return Employee(name, salary, age)

def input_employee_list():
    num_employees = int(input("Enter the number of employees: "))
    employees = []
    
    for i in range(1, num_employees + 1):
        print(f"Enter employee {i}")
        employees.append(input_employee())
    
    return employees

def print_employee_list(employees):
    for i, employee in enumerate(employees, 1):
        print(f"Employee {i}")
        print(employee.name)
        print(employee.salary)
        print(employee.age)

def sort_employees_by_age(employees):
    return sorted(employees, key=lambda x: x.age, reverse=True)

if __name__ == "__main__":
    print("1. Test f1 (1 point)")
    print("2. Test f2 (2 points)")
    print("3. Test f3 (1 point)")

    selection = int(input("Your selection (1 -> 3): "))

    if selection == 1:
        employees = input_employee_list()
        print("OUTPUT")
        print_employee_list(employees)
        print("FINISH")

    elif selection == 2:
        employees = input_employee_list()
        sorted_employees = sort_employees_by_age(employees)
        print("OUTPUT")
        print_employee_list(sorted_employees)
        print("FINISH")

    elif selection == 3:
        pass

    else:
        print("Invalid selection.")
