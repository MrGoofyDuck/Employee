from empl import Employee
from empo import EmployeeDAO
from datetime import datetime
def main():
    dao = EmployeeDAO('data.db')

    
    # Insert new employees
    new_employee1 = Employee(None, "Alice Smith", "Data Scientist", 95000, datetime.now().strftime("%Y-%m-%d"))
    new_employee2 = Employee(None, "Bob Johnson", "Software Engineer", 88000, datetime.now().strftime("%Y-%m-%d"))

    print(dao.insert(new_employee1))
    print(dao.insert(new_employee2))
    print("Employees added!")
    
    # Retrieve all employees
    employees = dao.get_all()
    print("All Employees:")
    for emp in employees:
        print(emp)
    
    # Retrieve an employee by ID
    emp = dao.get_by_id(1)
    if emp:
       print("Found Employee:", emp)
    
    # Update an employee
    if emp:
        emp.salary = 100000.0
        dao.update(emp)
        print("Employee updated:", dao.get_by_id(1))
    
    # Delete an employee
    dao.delete(1)
    print("Employee deleted!")
    
    # Close the database connection
    dao.close()

if __name__ == "__main__":
    main()

