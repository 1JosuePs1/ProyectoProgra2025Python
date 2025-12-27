Task Management System (Ufidelitas)

This is a basic programming final project developed in Python. It is a console-based application designed to manage tasks, allowing control over priorities, statuses (Pending, Active, Completed), and specific categories.

Features
- **Login System:** User registration and login with attempt validation.
- **Task Management:** Create tasks with title, description, dates, and priorities.
- **Tracking:** Real-time updates for task status and priority.
- **Statistical Reports:** Visualization of completion percentages and task counts by category (Work/Study, Personal/Home, Health/Wellness).

Project Structure
- `inicio.py`: Program entry point and user management.
- `menuPrincipal.py`: Navigation control between modules.
- `registroTareas.py`: Logic for capturing new tasks.
- `asignarEstado.py`: Module for updating status and priorities.
- `verTareas.py`: Filter to view non-completed tasks.
- `informes.py`: Statistics generation.
- `variables.py`: Global data storage.

Requirements
- Python 3.x installed.

Installation and Usage
1. Clone this repository:
   `git clone https://github.com/1JosuePs1/ProyectoProgra2025Python.git`
2. Navigate to the folder:
   `cd ProyectoProgra2025Python`
3. Run the program:
   `python inicio.py`
