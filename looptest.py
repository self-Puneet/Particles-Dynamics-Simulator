import tkinter as tk

def increment():
    global i
    i += 1
    label.config(text=f"Value of i: {i}")


# Create the main window
root = tk.Tk()
root.title("Manual Loop Control Example")

i = 0

while i < 5:
    print("nasu")
    next_button = tk.Button(root, text="Next", command=increment)

# Initialize the variable

# Create a label to display the value of i
label = tk.Label(root, text=f"Value of i: {i}")
label.pack(pady=10)

# Create a button to manually trigger the next cycle
next_button.pack(pady=10)

# Start the Tkinter main loop
root.mainloop()
