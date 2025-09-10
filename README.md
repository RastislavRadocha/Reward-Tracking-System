Here’s a clear and concise `README.md` description for your **Tracking/Reward System** project:

---

# 🏆 Tracking & Reward System

A desktop productivity tool built with **Python** and **Tkinter** that tracks which application is currently active on your screen and rewards you with points based on the time spent in approved (productive) programs.

---

## 💡 Features

* 🖥️ **Active Window Monitoring**
  Detects and displays the title of the currently active program window.

* ⏱️ **Time Tracking**
  Tracks how long each productive app is being used.

* 🎯 **Customizable Productivity List**
  Add keywords or app names to define what counts as "productive".

* 🎁 **Reward System**
  Earn points over time based on your focus in productive applications.

* 🧩 **Tkinter GUI**
  Clean and simple interface to view tracked time, current active app, and total points.

## 🛠️ Technologies Used

* Python 3
* Tkinter (GUI)
* `pywin32` (`win32gui`) for Windows window tracking

## 🚧 Current Status

* Basic GUI and active window display implemented
* Time tracking and app filtering in progress
* Multi-threading and persistent storage (optional) to be added


## 📦 Setup & Run

1. Clone the repository

   ```bash
   git clone https://github.com/yourusername/tracker-system.git
   ```

2. Navigate to the project folder

   ```bash
   cd tracker-system
   ```

3. Install dependencies

   ```bash
   pip install pywin32
   ```

4. Run the application

   ```bash
   python main.py
   ```

## 🔒 Platform Compatibility

> ✅ Currently works on **Windows only**, due to use of `win32gui` for active window tracking.


## 📌 To-Do

* [ ] Add start/stop logging buttons
* [ ] Threaded tracking loop to prevent GUI freezing
* [ ] Persistent point storage (e.g. save to file or database)
* [ ] Configurable reward rules

