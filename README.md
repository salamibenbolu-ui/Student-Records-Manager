# Student Records Manager

A simple command-line Student Records Manager built with Python as part of my 100 Days of Python learning journey (Day 34/100).

The project demonstrates how lists and dictionaries can work together to store, organise, and retrieve student information.

## Features

- Add new student records.
- Store student names and scores.
- View all registered students.
- Search for a student by name.
- Case-insensitive student name searching.
- Interactive menu-driven interface.

## Technologies Used

- Python 3
- Lists
- Dictionaries
- While loops
- For loops
- Conditional statements
- User input and string methods

## Project Structure

```text
Student-Records-Manager/
│
└── main.py
```

## Getting Started

### Prerequisites

- Python 3 installed on your computer.

### Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/salamibenbolu-ui/Student-Records-Manager.git
   ```

2. Navigate into the project directory:

   ```bash
   cd Student-Records-Manager
   ```

3. Run the program:

   ```bash
   python main.py
   ```

## How to Use

When the program starts, you'll see the following menu:

```text
===== STUDENTS RECORD MANAGER =====
1. Add student
2. View all students
3. Search student
4. Exit
```

- Select **1** to add a student's name and score.
- Select **2** to display all student records.
- Select **3** to search for a student by name.
- Select **4** to exit the program.

## How Student Records Are Stored

Each student is represented by a dictionary containing their name and score.

Multiple student dictionaries are stored inside a list.

Example:

```python
students = [
    {"name": "Benjamin", "score": 85.0},
    {"name": "John", "score": 72.5}
]
```

## What I Learned

Through this project, I practised:

- Combining lists and dictionaries.
- Creating and accessing dictionary values.
- Adding dictionaries to a list.
- Iterating through lists of dictionaries.
- Searching through stored records.
- Using conditional statements and loops.
- Accepting and processing user input.

## Current Limitations

- Student records are stored in memory and are not saved after the program closes.
- The program expects valid numeric input for menu choices and student scores.
- Each student is currently identified by their name during searches.

## Future Improvements

- Save student records using JSON.
- Add the ability to update student records.
- Add the ability to delete student records.
- Improve input validation.
- Calculate student averages and grades.

## Author

**Salami Benjamin**

GitHub: [@salamibenbolu-ui](https://github.com/salamibenbolu-ui)

## Learning Journey

Day 34 of 100 Days of Python.

