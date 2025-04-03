# Employee Management System

## Overview
This Python application interacts with an SQLite relational database to manage employee data. It implements CRUD (Create, Read, Update, Delete) operations for an `Employee` table using the `sqlite3` module. The project consists of an `Employee` entity class and an `EmployeeDAO` class to handle database operations.

## Features
- **Create**: Add a new employee to the database.
- **Read**: Retrieve an employee's details by ID or fetch all employees.
- **Update**: Modify an employee's details.
- **Delete**: Remove an employee from the database.

## Technologies Used
- **Python 3**
- **SQLite**

## Database Schema
The database is named `employee_db.sqlite`, and it contains the `employee` table with the following columns:

| Column   | Type    | Constraints |
|----------|--------|-------------|
| id       | INTEGER | PRIMARY KEY, AUTOINCREMENT |
| name     | TEXT   | NOT NULL    |
| position | TEXT   | NOT NULL    |
| salary   | REAL   | NOT NULL    |
| hire_date| TEXT   | NOT NULL    |


## How to Run the Project
1. **Clone the Repository**:
   ```sh
   git clone https://github.com/MrGoofyDuck/Employee.git
   cd Employee
   ```
2. **Run the Application**:
   ```sh
   python main.py
   ```

## CRUD Operations Demonstration
### 1. Insert a New Employee
```python
from employee import Employee
from employee_dao import EmployeeDAO

dao = EmployeeDAO()
new_employee = Employee(None, "John Doe", "Software Engineer", 75000, "2024-04-01")
dao.insert(new_employee)
```

### 2. Retrieve an Employee by ID
```python
employee = dao.get_by_id(1)
print(employee)
```

### 3. Retrieve All Employees
```python
employees = dao.get_all()
for emp in employees:
    print(emp)
```

### 4. Update Employee Details
```python
updated_employee = Employee(1, "John Doe", "Senior Software Engineer", 90000, "2024-04-01")
dao.update(updated_employee)
```

### 5. Delete an Employee
```python
dao.delete(1)
```

## Sample Output
```
Employee inserted successfully.
Employee(id=1, name='John Doe', position='Software Engineer', salary=75000, hire_date='2024-04-01')
All Employees: [(1, 'John Doe', 'Software Engineer', 75000, '2024-04-01')]
Employee updated successfully.
Employee deleted successfully.
```





