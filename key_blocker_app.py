import tkinter as tk
from tkinter import ttk, messagebox
import keyboard

class KeyBlockerApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("System-wide Key Blocker")
        self.geometry("420x320")
        self.resizable(False, False)

        self.disabled_keys = {}  # key -> True if blocked
        self._build_ui()
        self.bind_all("<Key>", self._tk_blocker, add="+")

    def _build_ui(self):
        tk.Label(self, text="Enter key to disable:").pack(pady=(15, 4))

        entry_frame = tk.Frame(self)
        entry_frame.pack()
        self.key_entry = ttk.Entry(entry_frame, width=25)
        self.key_entry.pack(side="left", padx=(0, 8))

        ttk.Button(entry_frame, text="Disable", command=self.disable_key).pack(side="left")
        ttk.Button(entry_frame, text="Enable Selected Key",  command=self.enable_selected_key ).pack(side="left")
        tk.Button(self, text="Enable All Keys", command=self.enable_all_keys,
          bg="orange", fg="black", font=("Segoe UI", 10, "bold")).pack(pady=(0, 10))

        # Grid (Treeview) to display disabled keys
        columns = ("#", "Key", "Status")
        self.table = ttk.Treeview(self, columns=columns, show="headings", height=9)
        self.table.heading("#", text="#")
        self.table.heading("Key", text="Key")
        self.table.heading("Status", text="Status")
        self.table.column("#", width=40, anchor="center")
        self.table.column("Key", width=140, anchor="center")
        self.table.column("Status", width=140, anchor="center")
        self.table.pack(pady=15, fill="x", padx=12)

        # Enable button for selected key
        #ttk.Button(self, text="Enable Selected Key", command=self.enable_selected_key).pack(pady=4)
      


        self.status_lbl = tk.Label(self, text="", fg="blue")
        self.status_lbl.pack(pady=(0, 10))

        style = ttk.Style(self)
        style.configure("Treeview", rowheight=24, font=("Segoe UI", 10))
        style.configure("Treeview.Heading", font=("Segoe UI", 10, "bold"))

    def disable_key(self):
        key = self.key_entry.get().strip().lower()
        if not key:
            messagebox.showwarning("Missing Input", "Please enter a key to disable.")
            return
        if self.disabled_keys.get(key):
            messagebox.showinfo("Already Disabled", f'"{key}" is already disabled.')
            return

        try:
            keyboard.block_key(key)
            self.disabled_keys[key] = True
            self._refresh_table()
            self.status_lbl.config(text=f'Key "{key}" has been disabled.')
            self.key_entry.delete(0, tk.END)  # Clear input field
        except ValueError as e:
            messagebox.showerror("Invalid Key", str(e))

    def enable_selected_key(self):
        selected = self.table.selection()
        if not selected:
            messagebox.showinfo("No Selection", "Please select a key to enable from the list.")
            return

        key = self.table.item(selected[0])["values"][1]
        if self.disabled_keys.get(key):
            keyboard.unblock_key(key)
            self.disabled_keys[key] = False
            self._refresh_table()
            self.status_lbl.config(text=f'Key "{key}" has been enabled.')

    def _refresh_table(self):
        self.table.delete(*self.table.get_children())
        for idx, (key, status) in enumerate(self.disabled_keys.items(), start=1):
            if status:
                self.table.insert("", "end", values=(idx, key, "Disabled"))

    def _tk_blocker(self, event):
        """Block keys even inside Tkinter UI"""
        if self.disabled_keys.get(event.keysym.lower()):
            return "break"
    
    def enable_all_keys(self):
        if not self.disabled_keys:
            messagebox.showinfo("Info", "No keys are currently disabled.")
            return

        for key, status in list(self.disabled_keys.items()):
            if status:
                keyboard.unblock_key(key)
                self.disabled_keys[key] = False

        self._refresh_table()
        self.status_lbl.config(text="All keys have been enabled.")


if __name__ == "__main__":
    try:
        app = KeyBlockerApp()
        app.mainloop()
    except PermissionError:
        print("Please run this script as Administrator to enable system-wide key blocking.")
