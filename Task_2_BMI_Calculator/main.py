import tkinter as tk
from tkinter import ttk, messagebox
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from working import *

root = tk.Tk()
root.title("BMI Calculator")
root.geometry("250x300")


def show_bmi():
    name = name_entry.get()
    try:
        weight = float(weight_entry.get())
        height = float(height_entry.get())
    except ValueError:
        messagebox.showerror("Input Error", "Please enter valid numbers for weight and height.")
        return

    bmi = calculate_bmi(weight, height)
    result_label.config(text=f"BMI: {bmi}")

    save_bmi_data(name, weight, height, bmi)
    messagebox.showinfo("BMI Result", f"{name}, your BMI is {bmi}")


def show_history():
    name = name_entry.get()
    data = retrieve_data(name)
    if not data:
        messagebox.showinfo("No Data", "No historical data found for this user.")
        return

    history_window = tk.Toplevel(root)
    history_window.title("Historical Data")

    columns = ("Date", "Weight", "Height", "BMI")
    tree = ttk.Treeview(history_window, columns=columns, show="headings")
    tree.heading("Date", text="Date")
    tree.heading("Weight", text="Weight")
    tree.heading("Height", text="Height")
    tree.heading("BMI", text="BMI")

    for row in data:
        tree.insert("", tk.END, values=(row[5], row[2], row[3], row[4]))

    tree.pack(expand=True, fill=tk.BOTH)


def plot_bmi_trend():
    name = name_entry.get()
    data = retrieve_data(name)
    if not data:
        messagebox.showinfo("No Data", "No historical data found for this user.")
        return

    dates = [row[5] for row in data]
    bmi = [row[4] for row in data]

    plt.figure(figsize=(10, 5))
    plt.plot(dates, bmi, marker='o', linestyle='-', color='b')
    plt.xlabel('Date')
    plt.ylabel('BMI')
    plt.title('BMI Trend')
    plt.xticks(rotation=45)
    plt.tight_layout()

    trend_window = tk.Toplevel(root)
    trend_window.title("BMI Trend")

    fig = plt.gcf()
    canvas = FigureCanvasTkAgg(fig, master=trend_window)
    canvas.draw()
    canvas.get_tk_widget().pack(expand=True, fill=tk.BOTH)


tk.Label(root, text="Name:").grid(row=0, column=0, padx=10, pady=10)
name_entry = tk.Entry(root)
name_entry.grid(row=0, column=1, padx=10, pady=10)

tk.Label(root, text="Weight (kg):").grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

tk.Label(root, text="Height (cm):").grid(row=2, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=2, column=1, padx=10, pady=10)

calculate_button = tk.Button(root, text="Calculate BMI", command=show_bmi)
calculate_button.grid(row=3, column=0, columnspan=2, pady=10)

result_label = tk.Label(root, text="BMI: ", font=('Helvetica', 16))
result_label.grid(row=4, column=0, columnspan=2, pady=10)

history_button = tk.Button(root, text="View History", command=show_history)
history_button.grid(row=5, column=0, pady=10)

trend_button = tk.Button(root, text="View Trend", command=plot_bmi_trend)
trend_button.grid(row=5, column=1, pady=10)


root.mainloop()
conn.close()
