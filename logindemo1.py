import tkinter as tk
from tkinter import messagebox

# ---------------- CONFIG ----------------
MAX_ATTEMPTS = 3
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

attempts_left = MAX_ATTEMPTS

# ---------------- FUNCTIONS ----------------
def login(event=None):
    global attempts_left

    username = entry_user.get().strip()
    password = entry_pass.get().strip()

    # Empty field check
    if not username or not password:
        messagebox.showwarning("Warning", "Please fill all fields ⚠️")
        return

    # Correct credentials
    if username == VALID_USERNAME and password == VALID_PASSWORD:
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

# ---------------- UI SETUP ----------------
root = tk.Tk()
root.title("Login System v2")
root.geometry("320x240")
root.resizable(False, False)

# Title
tk.Label(
    root,
    text="Secure Login",
    font=("Arial", 18, "bold")
).pack(pady=10)

# Username
tk.Label(root, text="Username").pack(anchor="w", padx=30)
entry_user = tk.Entry(root, width=25)
entry_user.pack(pady=3)

# Password
tk.Label(root, text="Password").pack(anchor="w", padx=30)
entry_pass = tk.Entry(root, show="*", width=25)
entry_pass.pack(pady=3)

# Show/Hide Password Button
toggle_btn = tk.Button(
    root,
    text="Show",
    width=8,
    command=toggle_password
)
toggle_btn.pack(pady=5)

# Login Button
login_btn = tk.Button(
    root,
    text="Login",
    width=15,
    command=login
)
login_btn.pack(pady=10)

# Bind Enter key
root.bind("<Return>", login)

# Focus cursor on username
entry_user.focus()

# Run app
root.mainloop()
