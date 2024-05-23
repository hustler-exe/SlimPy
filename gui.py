# gui.py
import tkinter as tk
from tkinter import messagebox
from calculations import calculate_bmi
from db import insert_data, get_history
import matplotlib.pyplot as plt
def submit_data():
    try:
        name = entry_name.get()
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive values.")

        bmi, category = calculate_bmi(weight, height)

        # Insert data into the database
        insert_data(name, height, weight, bmi, category)

        messagebox.showinfo("Result", f"Name: {name}\nBMI: {bmi:.2f}\nCategory: {category}")
        entry_name.delete(0, tk.END)
        entry_height.delete(0, tk.END)
        entry_weight.delete(0, tk.END)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def show_history(root):
    rows = get_history()

    if rows:
        history_window = tk.Toplevel(root)
        history_window.title("BMI History")

        text = tk.Text(history_window)
        text.pack(fill=tk.BOTH, expand=True)

        for row in rows:
            text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Height: {row[2]}, Weight: {row[3]}, BMI: {row[4]:.2f}, Category: {row[5]}, Date: {row[6]}\n")
    else:
        messagebox.showinfo("History", "No historical data available.")

def visualize_trends():
    rows = get_history()

    if rows:
        dates = [row[6] for row in rows]
        bmis = [row[4] for row in rows]

        plt.figure(figsize=(10, 5))
        plt.plot(dates, bmis, marker='o')
        plt.title("BMI Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        messagebox.showinfo("Trends", "No data available for visualization.")

def run_gui():
    root = tk.Tk()
    root.title("BMI Calculator")

    tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
    global entry_name
    entry_name = tk.Entry(root)
    entry_name.grid(row=0, column=1, padx=10, pady=10)

    tk.Label(root, text="Height (m):").grid(row=1, column=0, padx=10, pady=10)
    global entry_height
    entry_height = tk.Entry(root)
    entry_height.grid(row=1, column=1, padx=10, pady=10)

    tk.Label(root, text="Weight (kg):").grid(row=2, column=0, padx=10, pady=10)
    global entry_weight
    entry_weight = tk.Entry(root)
    entry_weight.grid(row=2, column=1, padx=10, pady=10)

    tk.Button(root, text="Calculate BMI", command=submit_data).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Show History", command=lambda: show_history(root)).grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Visualize Trends", command=visualize_trends).grid(row=5, column=0, columnspan=2, pady=10)

    root.mainloop()
