# Browser Automation Software v2

> A personal automation cockpit for speed, privacy, and control.

**Browser Automation Software v2** is a desktop productivity tool built in Python that brings together browser automation, encrypted storage, monitoring, clipboard capture, secure notes, screenshot handling, and image-based login assistance in one place.

It is designed for users who want to move faster while keeping sensitive data organized and protected.

---

## What this project does

This app is more than a browser helper. It acts like a private command center for daily digital work:

- Captures and stores clipboard data in encrypted form
- Manages encrypted authentication details for websites and apps
- Saves notes in plain text or encrypted format
- Organizes screenshots into folder-based collections
- Stores visual descriptions linked to image sets
- Tracks usage, time, memory, and internet activity
- Supports quick automation actions through keyboard shortcuts
- Helps fill login fields using image detection and clipboard actions

---

## Features

### 🔐 Encryption-first design
Sensitive data is stored in encrypted files using password-based key derivation and Fernet encryption.

### 📋 Clipboard vault
Every copied item can be captured, encrypted, viewed later, copied back, or deleted in ranges.

### 🧾 Secure authentication manager
Save website usernames and passwords, decrypt them when needed, edit entries, and auto-fill fields with shortcut-based actions.

### 📝 Notes system
Write notes in the built-in editor, save them as normal text files, or store them encrypted.

### 🖼 Screenshot and visual memory tools
Group screenshots into folders, browse them later, and attach descriptive notes to image collections.

### 📊 Monitoring panel
Track:
- data usage
- time usage
- average internet usage
- memory usage
- estimated exhaustion time

### ⌨️ Shortcut-driven workflow
The app includes keyboard-driven actions for quick closing, clipboard capture, screenshot capture, and form-filling operations.

### 🗂 Folder and cache management
The program creates and maintains the folders and cache files it needs automatically on startup.

---

## Built With

- Python
- Tkinter
- CustomTkinter
- PyAutoGUI
- Psutil
- Cryptography
- Pillow
- Requests
- BeautifulSoup
- Matplotlib
- Keyboard
- Pyperclip

---

## Main capabilities

- Browser/window automation
- Encrypted clipboard logging
- Encrypted login storage
- Image-based login assistance
- Screenshot capture and grouping
- Visual note attachment
- Plain and encrypted note storage
- To-do list support
- Usage monitoring and graphing

---

## How it works

The app creates its required folders and files automatically when it starts.

It uses a master password system to derive encryption keys, then stores protected data in dedicated folders such as:

- encrypted clipboards
- encrypted screenshots
- encrypted authentication details
- encrypted written notes
- encrypted visual descriptive writings

This makes the project feel like a compact personal workspace rather than a single-purpose script.

---

## Keyboard shortcuts

Some actions are triggered from the keyboard for speed.

Examples include:
- closing the active window
- saving clipboard data
- marking screenshot regions
- triggering image detection actions
- disabling image detection

---

## Why this project is interesting

This project blends a lot of powerful ideas into one app:

- automation
- privacy
- local storage
- UI tooling
- image recognition workflows
- personal productivity

It feels like a custom-built assistant for people who want more control over their browser sessions and personal workflow.

---

## Project structure

At runtime, the app creates and uses several folders, including:

- `All text files from TakeNote`
- `Browser automation software stored encrypted files`
- `Browser automation important cache files`
- `Folder Holding Files`
- `Images for Detection`
- `To-do list folder`

---

## Security note

This project is built around local encrypted storage, but it is still important to keep your master password safe. If the master key is reset, the app clears stored encrypted content to protect privacy.


---

## License

MIT
---

## Author

Made by Raakin Khan
a ex student of dps bn,
current rvpu bn
