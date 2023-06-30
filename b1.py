class Employee:
    def init(self, empno, name, depname, designation, age, salary):
        self.empno = empno
        self.name = name
        self.depname = depname
        self.designation = designation
        self.age = age
        self.salary = salary

    def accept_details(self):
        self.empno = input("Enter employee number: ")
        self.name = input("Enter employee name: ")
        self.depname = input("Enter department name: ")
        self.designation = input("Enter designation: ")
        self.age = input("Enter age: ")
        self.salary = input("Enter salary: ")

    def search_employee(self, empno):
        for employee in employees:
            if employee.empno == empno:
                return employee

    def display_details(self):
        print("Employee number:", self.empno)
        print("Employee name:", self.name)
        print("Department name:", self.depname)
        print("Designation:", self.designation)
        print("Age:", self.age)
        print("Salary:", self.salary)



employees = []

s
for i in range(int(input("Enter number of employees: "))):
    employee = Employee()
    employee.accept_details()
    employees.append(employee)


empno = input("Enter employee number to search: ")
employee = employee.search_employee(empno)
# Display the details of the employee
if employee is not None:
    print("Employee details:")
    employee.display_details()
else:
    print("Employee not found!")
