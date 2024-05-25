# Import necessary modules
import tkinter as tk
from tkinter import messagebox
from calculations import calculate_bmi  # Import function for calculating BMI
from db import insert_data, get_history  # Import functions for database operations
import matplotlib.pyplot as plt

# Function to handle submission of BMI data
def submit_data():
    try:
        # Retrieve input data from entry fields
        name = entry_name.get()
        height = float(entry_height.get())
        weight = float(entry_weight.get())

        # Check if height and weight are positive values
        if height <= 0 or weight <= 0:
            raise ValueError("Height and weight must be positive values.")

        # Calculate BMI and determine category
        bmi, category = calculate_bmi(weight, height)

        # Insert data into the database
        insert_data(name, height, weight, bmi, category)

        # Display result using a message box
        messagebox.showinfo("Result", f"Name: {name}\nBMI: {bmi:.2f}\nCategory: {category}")

        # Clear entry fields after submission
        entry_name.delete(0, tk.END)
        entry_height.delete(0, tk.END)
        entry_weight.delete(0, tk.END)
    except ValueError as e:
        # Display error message if input data is invalid
        messagebox.showerror("Input Error", str(e))

# Function to display historical BMI data
def show_history(root):
    # Retrieve historical data from the database
    rows = get_history()

    if rows:
        # Create a new window to display historical data
        history_window = tk.Toplevel(root)
        history_window.title("BMI History")

        # Create a text widget to display data
        text = tk.Text(history_window)
        text.pack(fill=tk.BOTH, expand=True)

        # Display each row of historical data
        for row in rows:
            text.insert(tk.END, f"ID: {row[0]}, Name: {row[1]}, Height: {row[2]}, Weight: {row[3]}, BMI: {row[4]:.2f}, Category: {row[5]}, Date: {row[6]}\n")
    else:
        # Display message if no historical data is available
        messagebox.showinfo("History", "No historical data available.")

# Function to visualize BMI trends over time
def visualize_trends():
    # Retrieve historical data from the database
    rows = get_history()

    if rows:
        # Extract dates and BMI values from historical data
        dates = [row[6] for row in rows]
        bmis = [row[4] for row in rows]

        # Plot BMI trends over time
        plt.figure(figsize=(10, 5))
        plt.plot(dates, bmis, marker='o')
        plt.title("BMI Trend Over Time")
        plt.xlabel("Date")
        plt.ylabel("BMI")
        plt.xticks(rotation=45)
        plt.tight_layout()
        plt.show()
    else:
        # Display message if no data is available for visualization
        messagebox.showinfo("Trends", "No data available for visualization.")

# Function to run the GUI application
def run_gui():
    # Create the main application window
    root = tk.Tk()
    root.title("SlimPy (BMI-Calculator)")

    # Create labels and entry fields for name, height, and weight
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

    # Create buttons for BMI calculation, displaying history, and visualizing trends
    tk.Button(root, text="Calculate BMI", cursor="hand2", command=submit_data).grid(row=3, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Show History", cursor="hand2", command=lambda: show_history(root)).grid(row=4, column=0, columnspan=2, pady=10)
    tk.Button(root, text="Visualize Trends", cursor="hand2", command=visualize_trends).grid(row=5, column=0, columnspan=2, pady=10)

    # Run the main event loop
    root.mainloop()
