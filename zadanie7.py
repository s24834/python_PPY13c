import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import csv

def connect_db() -> tuple[sqlite3.Connection, sqlite3.Cursor]:
    try:
        conn = sqlite3.connect('students.sqlite')
        cur = conn.cursor()
        cur.execute('''CREATE TABLE IF NOT EXISTS students
                    (email TEXT PRIMARY KEY, first_name TEXT, surname TEXT, points INTEGER, grade REAL, status TEXT)''')
        conn.commit()
    except sqlite3.Error as e:
        raise e
    return conn, cur

def insert_data(email, first_name, surname, points, grade, status):
    conn, cur = connect_db()
    try:
        cur.execute("INSERT INTO students VALUES (?, ?, ?, ?, ?, ?)", (email, first_name, surname, points, grade, status))
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred while inserting data: {e}")
    finally:
        conn.close()

def update_data(email, first_name, surname, points, grade, status):
    conn, cur = connect_db()
    try:
        cur.execute("UPDATE students SET first_name=?, surname=?, points=?, grade=?, status=? WHERE email=?", (first_name, surname, points, grade, status, email))
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred while updating data: {e}")
    finally:
        conn.close()

def delete_data(email):
    conn, cur = connect_db()
    try:
        cur.execute("DELETE FROM students WHERE email=?", (email,))
        conn.commit()
    except sqlite3.Error as e:
        messagebox.showerror("Error", f"An error occurred while deleting data: {e}")
    finally:
        conn.close()

def fetch_data():
    conn, cur = connect_db()
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    conn.close()
    return rows

def export_csv():
    data = fetch_data()
    with open('students.csv', 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Email', 'First Name', 'Surname', 'Points', 'Grade', 'Status'])
        for row in data:
            writer.writerow(row)
    messagebox.showinfo("Success", "Data exported to students.csv")

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import sqlite3
import csv

def refresh_data():
    tree.delete(*tree.get_children())
    for row in fetch_data():
        tree.insert('', 'end', values=row)

def add_student():
    insert_data(email_var.get(), first_name_var.get(), surname_var.get(), int(points_var.get()), float(grade_var.get()), status_var.get())
    refresh_data()

def update_student():
    update_data(email_var.get(), first_name_var.get(), surname_var.get(), int(points_var.get()), float(grade_var.get()), status_var.get())
    refresh_data()

def delete_student():
    delete_data(email_var.get())
    refresh_data()

def on_tree_select(event):
    item = tree.focus()
    values = tree.item(item, 'values')
    if values:
        email_var.set(values[0])
        first_name_var.set(values[1])
        surname_var.set(values[2])
        points_var.set(values[3])
        grade_var.set(values[4])
        status_var.set(values[5])

root = tk.Tk()
root.title("Student Database")

frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

email_var = tk.StringVar()
first_name_var = tk.StringVar()
surname_var = tk.StringVar()
points_var = tk.StringVar()
grade_var = tk.StringVar()
status_var = tk.StringVar()

ttk.Label(frame, text="Email:").grid(column=0, row=0, sticky=tk.W)
ttk.Entry(frame, textvariable=email_var).grid(column=1, row=0, sticky=(tk.W, tk.E))

ttk.Label(frame, text="First Name:").grid(column=0, row=1, sticky=tk.W)
ttk.Entry(frame, textvariable=first_name_var).grid(column=1, row=1, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Surname:").grid(column=0, row=2, sticky=tk.W)
ttk.Entry(frame, textvariable=surname_var).grid(column=1, row=2, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Points:").grid(column=0, row=3, sticky=tk.W)
ttk.Entry(frame, textvariable=points_var).grid(column=1, row=3, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Grade:").grid(column=0, row=4, sticky=tk.W)
ttk.Entry(frame, textvariable=grade_var).grid(column=1, row=4, sticky=(tk.W, tk.E))

ttk.Label(frame, text="Status:").grid(column=0, row=5, sticky=tk.W)
ttk.Entry(frame, textvariable=status_var).grid(column=1, row=5, sticky=(tk.W, tk.E))

ttk.Button(frame, text="Add", command=add_student).grid(column=0, row=6, sticky=tk.W)
ttk.Button(frame, text="Update", command=update_student).grid(column=1, row=6, sticky=tk.W)
ttk.Button(frame, text="Delete", command=delete_student).grid(column=2, row=6, sticky=tk.W)
ttk.Button(frame, text="Export CSV", command=export_csv).grid(column=3, row=6, sticky=tk.W)

tree = ttk.Treeview(root, columns=('Email', 'First Name', 'Surname', 'Points', 'Grade', 'Status'), show='headings')
tree.heading('Email', text='Email')
tree.heading('First Name', text='First Name')
tree.heading('Surname', text='Surname')
tree.heading('Points', text='Points')
tree.heading('Grade', text='Grade')
tree.heading('Status', text='Status')
tree.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))
tree.bind('<<TreeviewSelect>>', on_tree_select)

root.columnconfigure(0, weight=1)
root.rowconfigure(1, weight=1)

refresh_data()

root.mainloop()
