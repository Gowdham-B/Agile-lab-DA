import tkinter as tk
from tkinter import messagebox

# Login validation function
def login():
    username = entry_user.get()
    password = entry_pass.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login Status", "Login Successful ✅")
        root.destroy()  # Close window after success
    else:
        attempts_left -= 1
        if attempts_left > 0:
            messagebox.showerror(
                "Login Failed",
                f"Invalid credentials ❌\nAttempts left: {attempts_left}"
            )
        else:
            messagebox.showerror(
                "Access Denied",
                "Too many failed attempts 🚫"
            )
            root.destroy()

def toggle_password():
    if entry_pass.cget("show") == "":
        entry_pass.config(show="*")
        toggle_btn.config(text="Show")
    else:
        entry_pass.config(show="")
        toggle_btn.config(text="Hide")

# Create main window
root = tk.Tk()
root.title("Login System")
root.geometry("300x200")
root.resizable(False, False)

# Labels
tk.Label(root, text="Login", font=("Arial", 16)).pack(pady=10)

# Username
tk.Label(root, text="Username").pack(anchor="w", padx=30)
entry_user = tk.Entry(root, width=25)
entry_user.pack(pady=3)

tk.Label(root, text="Password").pack()
entry_pass = tk.Entry(root, show="*")
entry_pass.pack()

# Login Button
tk.Button(root, text="Login", command=login).pack(pady=15)

# Run the application
root.mainloop()
