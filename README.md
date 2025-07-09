# 🛡️ Key Disable App (Windows Only)

A simple GUI-based Windows application that allows users to **disable and enable specific keys** system-wide — including in browsers, editors, and games. This app is useful for preventing accidental key presses, customizing keyboard behavior, or creating a distraction-free environment.

---

## 📌 Features

- ✅ Disable any key system-wide (e.g., `a`, `t`, `Enter`, etc.)
- ✅ Enable disabled keys individually or all at once
- ✅ Clear and intuitive UI built with `tkinter`
- ✅ List of currently disabled keys shown in a grid


---

## 🚀 Upcoming Features (Planned)

- 🔘 Disable multiple keys at once (`a, b, enter`)
- 🖱️ Right-click context menu to re-enable keys
- 💾 Save/load disabled keys between sessions
- 🖥️ System tray integration
- 🔒 Autostart on Windows boot
- 🔐 Block special keys: `Ctrl+Alt+Del`, `Win`, function keys

---

## 💻 Requirements

- Python 3.8+
- Windows OS only
- Administrator access (for full key-block functionality)

### Install Dependencies

```bash
pip install keyboard
```

> ℹ️ Note: The `keyboard` module requires **admin privileges** to work system-wide.

---

## 🛠️ How to Run (From Source)

```bash
python key_blocker_app.py
```

Make sure to run the app with **Administrator privileges**.

---

## 📦 How to Build Executable (Optional)

If you want to create a `.exe`:

```bash
pip install pyinstaller
pyinstaller --noconfirm --onefile --windowed key_blocker_app.py
```

You’ll find the `.exe` in the `/dist` folder.

---

## 🔒 Preventing Multiple Instances

This app uses a lock file (`app.lock`) to ensure only **one instance** runs at a time. This prevents issues like one instance blocking a key and another not being aware.

---

## ❗ Disclaimer

- Use with caution. Disabling critical keys (like `Win`, `Ctrl`, or `Alt`) may affect usability.
- Always remember which keys are disabled — especially if you disable typing-related keys like `t`, `e`, or `Enter`.

---

## 📃 License

MIT License – feel free to use and modify.

---

## 👨‍💻 Author

**Umesh Randhe** – Built with ❤️ using Python and Tkinter.