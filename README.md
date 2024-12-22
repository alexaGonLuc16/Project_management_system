# Task Management System

This project is a task assignment system designed to manage employees, tasks, and projects efficiently. It allows for creating, assigning, and tracking tasks while managing employee skills and project requirements.

## Features

- **Employee Management**: Create and manage employees with their skills.
- **Task Management**: Create tasks, assign them to projects, and track deadlines.
- **Project Management**: Organize tasks into projects and assign employees accordingly.
- **Assignment Server**: An intelligent system for matching employees to tasks based on their skills.

## Installation

1. Clone the repository:  
   `git clone <repository-url>`
2. Navigate to the project directory:  
   `cd <project-directory>`
3. Create a virtual environment (optional but recommended):  
   `python -m venv venv`
4. Activate the virtual environment:  
   - On Windows: `venv\Scripts\activate`
   - On macOS/Linux: `source venv/bin/activate`
5. Install dependencies:  
   `pip install -r requirements.txt`

## Running Tests

To run the tests, use the following command from the root directory:
`python -m unittest discover -s tests -p "*.py" -v`

- With `pytest`:  
  `pytest`

## Future Improvements

- Advanced user and role management
- GUI for easier interaction
- Database integration for data persistence
- Automated task assignment algorithms
- Multi-language support
