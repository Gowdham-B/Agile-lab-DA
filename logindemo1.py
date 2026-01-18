import tkinter as tk
from tkinter import messagebox

#This is a simple login demo application using Tkinter
def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Status", "Login Successful ✅")
    else:
        messagebox.showerror("Login Status", "Invalid Username or Password ❌")

def clear_fields():
    entry_user.delete(0, tk.END)
    entry_pass.delete(0, tk.END)
    
root = tk.Tk()
root.title("Secure Login System very successful")   
root.geometry("320x250")
root.resizable(False, False)

tk.Label(root, text="Welcome", font=("Arial", 14)).pack(pady=5)
tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="Username").pack()
entry_user = tk.Entry(root)
entry_user.pack()

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack(pady=5)

tk.Button(root, text="Login", command=login).pack(pady=15)
tk.Button(root, text="Clear", command=clear_fields).pack()

root.bind("<Return>", login)

root.mainloop()
