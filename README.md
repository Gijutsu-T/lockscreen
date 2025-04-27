# 🛡️ Lockscreen - Screen Protection App

## About

My siblings were fond of constantly looking at my work and sometimes tampering with it when I left my laptop unattended.  
I created this tool to **protect my work** and **maintain my privacy** while I'm away.

This app fills the screen with a **hacker-style matrix background** and prompts anyone attempting to use the laptop for a **passcode**.

---

## Features

- ✅ Fullscreen, unclosable (almost) interface
- ✅ Matrix-style hacker green background
- ✅ Passcode prompt with two incorrect attempts leading to system **sleep**
- ✅ Secret owner escape combo (`Ctrl+Shift+Q`)
- ✅ Lightweight, fast, simple

---

## Known Limitations

**Currently, there are some ways someone could bypass the lock if they know what they're doing:**
- Using **Task Manager** (`Ctrl+Shift+Esc`) to force-quit the app.
- Using **Windows shortcuts** like `Win + [Number]` to open taskbar apps.
- Using **macOS Mission Control** (`Ctrl+Up`) or **Linux Alt+Tab** to switch apps.

---

## Planned Bypass Protection (for advanced users)

To make it more secure across platforms, you can implement additional protections:

### Windows

- **Disable Task Manager** temporarily:
    ```python
    import os
    os.system("REG add HKCU\\Software\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v DisableTaskMgr /t REG_DWORD /d 1 /f")
    ```
- **Block Win + [number] shortcuts:** (Hard to fully prevent without a native C++ driver; possible to intercept with advanced packages like `keyboard` in Python)

### macOS

- **Prevent app switching:**
    - Not natively possible from a Python app (would need macOS system permissions and low-level Objective-C code).

### Linux

- **Prevent Alt+Tab switching:** 
    - You can override the keybindings using `xmodmap` or use a fullscreen app window without borders to trap focus.
    - Example (terminal command):
      ```bash
      xmodmap -e "keycode 64 = NoSymbol"
      ```

---

## Installation

### Windows

```bash
# Install dependencies
pip install pillow
```
Run:
```bash
python main.py
```
OR create an executable:
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
```
Find your `.exe` inside `dist/`.

---

### macOS

```bash
# Install dependencies
brew install python3
pip3 install pillow
```
Run:
```bash
python3 main.py
```
To make it a standalone `.app` (optional):
```bash
pip install py2app
python3 setup.py py2app
```
*(You’ll need to create a basic `setup.py` for py2app.)*

---

### Linux (Ubuntu, Fedora, etc.)

```bash
# Install dependencies
sudo apt update
sudo apt install python3 python3-pip
pip3 install pillow
```
Run:
```bash
python3 main.py
```
Creating an executable (optional):
```bash
pip install pyinstaller
pyinstaller --onefile --noconsole main.py
```

---

## Usage Instructions

- **Launch the app**.
- **Enter your secure passcode**.
- **2 wrong attempts = your device will go to sleep** (saving your work!).
- **Emergency exit:** `Ctrl+Shift+Q` (only if you're the owner).

---

## Known Bypass Methods (and why mine is basic 😂)

| Method            | Windows Shortcut | Mac Shortcut          | Linux Shortcut           |
|:------------------|:------------------|:-----------------------|:--------------------------|
| Task Manager      | `Ctrl+Shift+Esc`   | `Cmd+Option+Esc`        | `Ctrl+Alt+Del` or `xkill`  |
| App Switching     | `Win + [Number]`   | `Ctrl+Up (Mission Ctrl)`| `Alt+Tab`                 |

**Note:**  
> This first version was intentionally simple because my siblings are not very tech-savvy 😆.  
> They don't even know these shortcuts exist, so I knew I didn't have to implement full OS-level protection (yet).  
> In future versions, advanced OS hookings and shortcut blocking might be implemented for ultimate security.

---

## Important

⚡ Make sure to choose a **very strong passcode** that no one can guess.  
⚡ Remember the **secret combo (`Ctrl+Shift+Q`)** to quickly exit in emergencies.  
⚡ If you're planning to use this in a serious environment (e.g., offices), **full hardening is recommended**.
