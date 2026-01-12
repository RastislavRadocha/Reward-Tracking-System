**Functions you used and what they do:**

**From win32gui module:**

- `win32gui.GetForegroundWindow()` - Gets the ID number of the window that's currently active/on top
- `win32gui.GetWindowText(window_handle)` - Takes a window ID and returns the actual title text of that window

**From tkinter module:**

- `tk.Entry.delete(start, end)` - Erases text from the Entry box between two positions
- `tk.Entry.insert(position, text)` - Puts new text into the Entry box at a specific position
- `window.after(milliseconds, function)` - Schedules a function to run after a delay (like setting a timer)
- `window.after_cancel(function id)` - Cancels a request for callback set up earlier with `window.after()`

**From time module:**

- `time.sleep(seconds)` - Pauses the program for a specified number of seconds (you had this in your original code)

**Your custom functions:**

- `program_tracker()` - Gets the current active window and returns its title as text
- `update_program_name()` - Gets current window title, clears the Entry box, puts new title in, then schedules itself to run again
- `def start_time_tracking()` - Start the time tracking
- `def time_tracker()` - Timer loop that updates elapsed time
- `def pause_time()` - Pause the timer
- `def resume_time()` - Resume the timer from where it was paused
- `def stop_tracker()` - Stop the timer and reset values
- `def total_points_sum_csv` -  Calculates the total sum of all points from previous sessions


**Key tkinter constants:**

- `tk.END` - Represents the very end position in a text widget
- `0` - Represents the very beginning position in a text widget

The magic happens in that `after()` function - it's what makes your program keep checking and updating instead of just checking once and stopping!