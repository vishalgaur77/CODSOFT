# ##calculator project  i am  vishal gaur
import tkinter as tk
import math
import winsound  # For button sound (Windows)

def sound():
    winsound.Beep(800, 80)

def press(key):
    sound()
    entry.insert(tk.END, key)

def clear():
    sound()
    entry.delete(0, tk.END)

def calculate():
    sound()
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, result)
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

def sci(func):
    sound()
    try:
        value = float(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, func(value))
    except:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

root = tk.Tk()
root.title("🔥 Ultimate Calculator")
root.geometry("360x520")
root.resizable(False, False)

# Gradient background
canvas = tk.Canvas(root, width=360, height=520)
canvas.pack(fill="both", expand=True)
canvas.create_rectangle(0, 0, 360, 520, fill="#0f2027", outline="")
canvas.create_rectangle(0, 260, 360, 520, fill="#203a43", outline="")

# Display
entry = tk.Entry(
    root,
    font=("Segoe UI", 22, "bold"),
    bg="#000000",
    fg="#00ffcc",
    bd=0,
    justify="right"
)
entry.place(x=20, y=20, width=320, height=60)

# Buttons frame
frame = tk.Frame(root, bg="#203a43")
frame.place(x=20, y=100, width=320, height=380)

buttons = [
    ('7',), ('8',), ('9',), ('/',),
    ('4',), ('5',), ('6',), ('*',),
    ('1',), ('2',), ('3',), ('-',),
    ('0',), ('C',), ('=',), ('+')
]

row = col = 0
for (text,) in buttons:
    if text == "=":
        cmd = calculate
        color = "#2ed573"
    elif text == "C":
        cmd = clear
        color = "#ff4757"
    else:
        cmd = lambda t=text: press(t)
        color = "#57606f"

    tk.Button(
        frame, text=text, bg=color, fg="white",
        font=("Segoe UI", 14, "bold"),
        width=6, height=2, bd=0, command=cmd
    ).grid(row=row, column=col, padx=5, pady=5)

    col += 1
    if col == 4:
        col = 0
        row += 1

# Scientific buttons
sci_frame = tk.Frame(root, bg="#203a43")
sci_frame.place(x=20, y=450, width=320, height=50)

tk.Button(sci_frame, text="sin", bg="#1e90ff", fg="white",
          font=("Segoe UI", 12, "bold"),
          command=lambda: sci(math.sin)).pack(side="left", expand=True, fill="both", padx=4)

tk.Button(sci_frame, text="cos", bg="#ffa502", fg="white",
          font=("Segoe UI", 12, "bold"),
          command=lambda: sci(math.cos)).pack(side="left", expand=True, fill="both", padx=4)

tk.Button(sci_frame, text="tan", bg="#ff6b81", fg="white",
          font=("Segoe UI", 12, "bold"),
          command=lambda: sci(math.tan)).pack(side="left", expand=True, fill="both", padx=4)

tk.Button(sci_frame, text="√", bg="#2ed573", fg="white",
          font=("Segoe UI", 12, "bold"),
          command=lambda: sci(math.sqrt)).pack(side="left", expand=True, fill="both", padx=4)

root.mainloop()
