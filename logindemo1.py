import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Status", "Login Successful ✅")
    else:
        messagebox.showerror("Login Status", "Invalid Username or Password ❌")


root = tk.Tk()
root.title("Login System")
root.geometry("300x200")
root.resizable(False, False)


tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

tk.Button(root, text="Login", command=login).pack(pady=15)


root.mainloop()
