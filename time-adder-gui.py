import datetime
import tkinter as tk
from tkinter import messagebox

def add_time():
    # Get the current time
    now = datetime.datetime.now()

    try:
        # Get the hours and minutes from the user input
        hours_to_add = int(hours_entry.get())
        minutes_to_add = int(minutes_entry.get())

        # Add the hours and minutes to the current time
        new_time = now + datetime.timedelta(hours=hours_to_add, minutes=minutes_to_add)

        # Check if the new time is on the same day as the current day
        if new_time.date() == now.date():
            # Display only the time in the result label with increased text size
            result_label.config(text="The new time is: \n" + new_time.strftime("%H:%M"), font=("Helvetica", 18))
        else:
            # Display both the date and time in the result label with increased text size
            result_label.config(text="The new time is: \n" + new_time.strftime("%Y-%m-%d %H:%M"), font=("Helvetica", 18))
    except ValueError:
        # Display an error message if the user enters invalid input
        messagebox.showerror("Error", "Please enter valid numbers for hours and minutes.")

# Create the main window
root = tk.Tk()
root.title("Time Calculator")

# Add padding inside the window
root.geometry("300x200")
root.config(padx=20, pady=20)

# Create labels and entry widgets for the user input
hours_label = tk.Label(root, text="Hours:")
hours_label.pack()
hours_entry = tk.Entry(root)
hours_entry.pack()

minutes_label = tk.Label(root, text="Minutes:")
minutes_label.pack()
minutes_entry = tk.Entry(root)
minutes_entry.pack()

# Create a button to calculate the new time
calculate_button = tk.Button(root, text="Calculate", command=add_time)
calculate_button.pack()

# Create a label to display the result with increased text size
result_label = tk.Label(root, text="")
result_label.pack()

# Start the main event loop
root.mainloop()