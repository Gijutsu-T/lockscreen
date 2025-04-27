import tkinter as tk
import random
import threading
import os
import time

# Configuration
CORRECT_PASSWORD = "sleepyhallow"
MAX_ATTEMPTS = 2
MATRIX_CHARS = "AIY∑BV9@#WΩXDEFCGθHJ45λKL%&MNZ0OPQR1236∞78$STU"

attempts = 0
unlocked = False

def check_password():
    global attempts, unlocked
    entered = password_entry.get()
    if entered == CORRECT_PASSWORD:
        unlocked = True
        root.destroy()
    else:
        attempts += 1
        if attempts >= MAX_ATTEMPTS:
            warning_label.config(text="Too many wrong attempts!\n\nSleeping...\n\nReporting to Shammah...")
            root.update()
            time.sleep(1.5)
            os.system('rundll32.exe powrprof.dll,SetSuspendState 0,1,0')
        else:
            warning_label.config(text=f"Wrong password! {MAX_ATTEMPTS - attempts} attempts left.")
            password_entry.delete(0, tk.END)

def emergency_unlock(event=None):
    global unlocked
    unlocked = True
    root.destroy()

def matrix_rain():
    canvas_width = root.winfo_width()
    canvas_height = root.winfo_height()
    columns = int(canvas_width / 10)
    drops = [0 for _ in range(columns)]

    while not unlocked:
        canvas.delete("all")
        for i in range(len(drops)):
            char = random.choice(MATRIX_CHARS)
            x = i * 10
            y = drops[i] * 10
            canvas.create_text(x, y, text=char, fill="lime", font=("Consolas", 10))
            drops[i] = drops[i] + 1 if random.random() > 0.05 else 0
        root.update()
        time.sleep(0.05)

# Main window
root = tk.Tk()
root.title("Access Locked")
root.attributes("-fullscreen", True)
root.configure(bg="black")
root.bind('<Control-Shift-Q>', emergency_unlock)  # Emergency exit combo

canvas = tk.Canvas(root, bg="black", highlightthickness=0)
canvas.pack(fill="both", expand=True)

frame = tk.Frame(root, bg="black")
frame.place(relx=0.5, rely=0.5, anchor="center")

label = tk.Label(frame, text="! SYSTEM LOCKED !\nEnter Passcode:", fg="lime", bg="black", font=("Consolas", 24))
label.pack(pady=10)

password_entry = tk.Entry(frame, show="*", font=("Consolas", 20), width=25, bg="black", fg="lime", insertbackground="lime")
password_entry.pack(pady=10)
password_entry.focus()

submit_btn = tk.Button(frame, text="Submit", command=check_password, font=("Consolas", 16), bg="black", fg="lime", highlightbackground="lime", activebackground="green")
submit_btn.pack(pady=10)

warning_label = tk.Label(frame, text="", fg="red", bg="black", font=("Consolas", 16))
warning_label.pack(pady=10)

# Start Matrix animation in a thread
threading.Thread(target=matrix_rain, daemon=True).start()

root.mainloop()
