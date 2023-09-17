import tkinter as tk
import calculations


def start_simulation():
    calculations.area()
    calculations.random_dots(int(entry_dot_count.get())+1,int(entry_update_freq.get()))



# Create a window
window = tk.Tk()
w = 200
h = 200

# Initialize the screen dimensions
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x_coordinate = (screen_width / 2) - (w / 2)
y_coordinate = (screen_height / 2) - (h / 2)
window.geometry("%dx%d+%d+%d" % (w, h, x_coordinate, y_coordinate))

# User input for the number of points and update frequency
label_dot_count = tk.Label(window, text="Number of Points:")
label_dot_count.pack()
entry_dot_count = tk.Entry(window)
entry_dot_count.pack()

label_update_freq = tk.Label(window, text="Update Frequency:")
label_update_freq.pack()
entry_update_freq = tk.Entry(window)
entry_update_freq.pack()


# Start button
start_button = tk.Button(window, text="Start Simulation",command=start_simulation)
start_button.pack()

# Reset button
reset_button = tk.Button(window, text="Reset")
reset_button.pack()

# Start the main loop
window.mainloop()