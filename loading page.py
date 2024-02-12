import tkinter as tk
from tkinter import ttk

class ProgressBarWithTrail:
    def __init__(self, master, width=400, height=40, progress_color="green", background_color="white", border_color="grey", border_width=2, padding=10):
        self.master = master
        self.width = width
        self.height = height
        self.progress_color = progress_color
        self.background_color = background_color
        self.border_color = border_color
        self.border_width = border_width
        self.padding = padding
        self.master.configure(bg=self.background_color)
        self.canvas = tk.Canvas(self.master, width=self.width, height=self.height, bg=self.background_color, highlightthickness=0)
        self.canvas.pack()
        self.background_rect = self.canvas.create_rectangle(
            self.padding, self.padding,
            self.width - self.padding, self.height - self.padding,
            outline="", fill=self.background_color
        )
        self.progress_bar = self.canvas.create_rectangle(
            self.padding, self.padding,
            self.padding, self.height - self.padding,
            outline=self.border_color, width=self.border_width, fill=self.progress_color
        )
        self.border_rect = None
        self.progress_label = tk.Label(self.master, text="", font=("Helvetica", 12), bg=self.background_color)
        self.progress_label.pack()
        self.progress = 0
        self.update_progress()

    def update_progress(self):
        self.progress += 1
        if self.progress <= 100:
            progress_width = (self.progress / 100) * (self.width - 2 * self.padding)
            self.canvas.coords(self.progress_bar, self.padding, self.padding, self.padding + progress_width, self.height - self.padding)
            self.update_progress_label()
            self.master.after(50, self.update_progress)
        else:
            self.destroy_widgets()
            self.show_enter_button()

    def update_progress_label(self):
        percentage = int((self.progress / 100) * 100)
        self.progress_label.config(text=f"{percentage}% Complete")

    def show_enter_button(self):
        remove_button = tk.Button(self.master, text="Let's Go", command=self.open_new_window)
        remove_button.pack(pady=10)

    def destroy_widgets(self):
        # Remove progress bar-related widgets
        self.canvas.destroy()
        self.progress_label.destroy()

    def open_new_window(self):
        # Open a new window using Toplevel
        new_window = tk.Toplevel(self.master)
        new_window.title("New Window")
        new_window.geometry("400x200")
        label = tk.Label(new_window, text="This is a completely different window.")
        label.pack()

def main():
    root = tk.Tk()
    root.title("3-D Physics Simulator")
    root.iconbitmap("project icon.ico")
    root.configure(padx=20, pady=20)
    root.configure(bg="white")
    image_path = "project image.png"
    loading_image = tk.PhotoImage(file=image_path)
    loading_image_label = tk.Label(root, image=loading_image, bg="white")
    loading_image_label.pack()
    progress_bar = ProgressBarWithTrail(root)
    root.minsize(width=1000, height=650)
    root.maxsize(width=1000, height=650)
    root.lift()
    root.update_idletasks()
    root.mainloop()

if __name__ == "__main__":
    main()
