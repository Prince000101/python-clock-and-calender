import tkinter as tk
from tkinter import messagebox
from time import strftime
from datetime import datetime
from tkcalendar import Calendar  # Import Calendar widget


def update_clock():
    current_time = strftime("%I:%M:%S %p")  # Change to 12-hour format
    time_label.config(text=current_time)
    root.after(1000, update_clock)


def show_date():
    current_date = datetime.now().strftime("%A, %d %B %Y")
    messagebox.showinfo("Today's Date", f"The current date is:\n{current_date}")


def close_app():
    root.destroy()


root = tk.Tk()
root.title("Clock")
root.geometry("410x630")
root.resizable(False, False)

# Dark theme background color
root.configure(bg="#121212")

# Time frame
time_frame = tk.Frame(root, bg="#121212", highlightbackground="#1E90FF", highlightthickness=3)
time_frame.pack(pady=10)

# Time label
time_label = tk.Label(
    time_frame,
    text="00:00:00",  # Initial text for the clock
    font=("Courier", 40, "bold"),
    fg="#1E90FF",  # Light blue text
    bg="#121212",  # Dark background
    padx=20,
    pady=20,
)
time_label.pack()

# Calendar frame with border
calendar_frame = tk.Frame(root, bg="#121212", highlightbackground="#1E90FF", highlightthickness=2)
calendar_frame.pack(pady=20, padx=10)

# Calendar label
calendar_label = tk.Label(
    calendar_frame, text="Select a Date", font=("Arial", 14), fg="#1E90FF", bg="#121212"
)
calendar_label.pack(pady=5)

# Calendar widget with custom styling
calendar = Calendar(
    calendar_frame,
    selectmode="day",
    year=datetime.now().year,
    month=datetime.now().month,
    day=datetime.now().day,
    font=("Arial", 16),
    headersbackground="#2F4F4F",  # Dark greenish headers
    headersforeground="white",
    weekendbackground="#FF6347",  # Tomato color for weekends
    weekendforeground="white",
    selectbackground="#1E90FF",  # Cyan color for selected dates
    selectforeground="black",
    othermonthbackground="#808080",  # Gray for other months
    othermonthforeground="white",
    background="#121212",  # Dark background
    foreground="white",
)
calendar.pack(pady=20, padx=20)

# Button frame for show date and get selected date buttons
button_frame = tk.Frame(root, bg="#121212")
button_frame.pack(pady=10)

# Button to show today's date
date_button = tk.Button(
    button_frame,
    text="Show Date",
    font=("Arial", 14, "bold"),
    command=show_date,
    bg="#1E90FF",  # Light blue background
    fg="white",
    activebackground="#3CB371",  # Active background color
    activeforeground="white",
    relief="raised",
    bd=3,
    padx=10,
    pady=5,
)
date_button.grid(row=0, column=0, padx=5)

# Function to get the selected date
def get_selected_date():
    selected_date = calendar.get_date()
    messagebox.showinfo("Selected Date", f"You selected: {selected_date}")

# Button to retrieve selected date
get_date_button = tk.Button(
    button_frame,
    text="Get Selected Date",
    font=("Arial", 12),
    command=get_selected_date,
    bg="#1E90FF",
    fg="white",
    relief="raised",
    bd=3,
)
get_date_button.grid(row=0, column=1, padx=5)

# Button to close the app
def confirm_close():
    answer = messagebox.askyesno("Confirm Exit", "Are you sure you want to close the app?")
    if answer:
        root.destroy()


close_button = tk.Button(
    root,
    text="Close App",
    font=("Arial", 14, "bold"),
    command=confirm_close,
    bg="#FF6347",  # Red for the close button
    fg="white",
    activebackground="#DC143C",  # Darker red for active state
    activeforeground="white",
    relief="raised",
    bd=3,
    padx=20,
    pady=5,
)
close_button.pack(pady=10)

# Start the clock update
update_clock()
root.mainloop()
