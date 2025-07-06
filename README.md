# Project 3: Library Book Management System

## Overview

This is a simple console-based Library Management System developed in Python using object-oriented programming. It allows users to manage books by adding, removing, issuing, and returning them. The system also calculates fines for late returns.

## Features

- Add and remove books using unique book IDs
- Issue one book per student with a due date of 7 days
- Return books and calculate fine (₹5 per late day)
- View list of available books
- View list of issued books with due dates
- Menu-based user interface

## Technologies Used

- **Python 3**
- `datetime` module for date and time operations

## How to Run

1. Open the terminal or command prompt.
2. Run the Python file named:

```bash
python library_system.py
```

3. Use the menu to perform actions like adding, issuing, or returning books.
4. Choose option 7 to exit.

## Notes

- Each student can issue only one book at a time.
- Data is stored in memory during the session (no database or file saving).
- This is a basic prototype suitable for small-scale use or learning purposes.
