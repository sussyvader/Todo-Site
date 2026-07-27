# 📝 Todo List

A simple Todo List web application built with Django that allows users to create, manage, and organize daily tasks.

## Features

- ➕ Add new tasks
- 📋 View all tasks
- ❌ Delete completed or unwanted tasks
- 💾 Data stored using SQLite
- 🎨 Clean and responsive interface

## Tech Stack

- Python
- Django
- HTML
- CSS
- SQLite

## Project Structure

```
PROJECT1/
├── ihatebengalis/
├── Todo/
├── static/
├── Templates/
├── manage.py
├── requirements.txt
└── README.md
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/your-username/todo-list.git
cd todo-list
```

2. Create a virtual environment

```bash
python -m venv venv
```

3. Activate the virtual environment

**Windows**

```bash
venv\Scripts\activate
```

**macOS/Linux**

```bash
source venv/bin/activate
```

4. Install dependencies

```bash
pip install -r requirements.txt
```

5. Apply migrations

```bash
python manage.py migrate
```

6. Run the development server

```bash
python manage.py runserver
```

7. Open your browser and visit

```
http://127.0.0.1:8000/
```

## Future Improvements

- User authentication
- Task editing
- Due dates and reminders
- Task categories
- Search and filtering
- Dark mode

## License

This project is intended for learning and educational purposes.