# import tkinter for creating GUI apps 
import tkinter as tk
from tkinter import filedialog, messagebox 

# Main window code
root = tk.Tk()
root.title("Yashu's Text Editor")
root.geometry("800x600")

# Track mode
dark_mode = False

# Create text area
text = tk.Text(
    root,
    wrap=tk.WORD,
    font=("Helvetica", 12),
    undo=True
)
text.pack(expand=True, fill=tk.BOTH)

# ------------------ FUNCTIONS ------------------

def new_file():
    text.delete(1.0, tk.END)

def open_file():
    file_path = filedialog.askopenfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "r") as file:
            text.delete(1.0, tk.END)
            text.insert(tk.END, file.read())

def save_file():
    file_path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text Files", "*.txt")]
    )

    if file_path:
        with open(file_path, "w") as file:
            file.write(text.get(1.0, tk.END))
        messagebox.showinfo("Info", "File saved successfully")

def exit_app():
    confirm = messagebox.askyesno("Exit", "Do you want to exit?")
    if confirm:
        root.quit()

# 🌙 Dark Mode Toggle
def toggle_dark_mode():
    global dark_mode

    if dark_mode:
        # Light mode
        text.config(bg="white", fg="black", insertbackground="black")
        dark_mode = False
    else:
        # Dark mode
        text.config(bg="#1e1e1e", fg="white", insertbackground="white")
        dark_mode = True

# ------------------ MENU ------------------

menu = tk.Menu(root)
root.config(menu=menu)

# File Menu
file_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=file_menu)

file_menu.add_command(label="New", command=new_file)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=exit_app)

# View Menu (NEW)
view_menu = tk.Menu(menu, tearoff=0)
menu.add_cascade(label="View", menu=view_menu)

view_menu.add_command(label="Toggle Dark Mode", command=toggle_dark_mode)

# ------------------ SHORTCUT KEYS ------------------

root.bind("<Control-n>", lambda event: new_file())
root.bind("<Control-o>", lambda event: open_file())
root.bind("<Control-s>", lambda event: save_file())

# ------------------ RUN APP ------------------

root.mainloop()