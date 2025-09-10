import tkinter as tk
import time
import win32gui


def program_tracker():
    current_program = win32gui.GetForegroundWindow()  # Gets the ID number of the window that is on top
    current_program_title = win32gui.GetWindowText(current_program)  # Gets the name of the window/program/website page
    # print(current_program_title)  # Prints the title to console for testing purposes
    return current_program_title  # returns the variable to actually use it


def update_program_name():  # function for updating the name in the TkInter window
    active_program = program_tracker()  # calls the program_tracker() function
    active_program_entry.delete(0, tk.END)  # delete everything at index 0 to the END
    active_program_entry.insert(0, active_program)  # reinsert the name of the program
    window.after(1000, update_program_name)  # repeat the function and sending it to the Tk.Inter window every second



tracker_active = False # global variable for the tracking mechanism, set to False initially
start_time = 0 #  GLOBAL variable, used as a placeholder for further modification within function
time_display = "0:00" # GLOBAL variable for resetting the time entry
time_after_id = None # GLOBAL variable for saving .after id
elapsed_time_global = 0

def start_time_tracking():
    global tracker_active, start_time
    tracker_active = True # Set tracking flag to active
    start_time = time.time() # Record the current time as start time
    time_tracker() # Begin the timer loop



def time_tracker():  # function for tracking time
    global time_display, time_after_id, elapsed_time_global
    current_time = time.time() # Get current time
    elapsed_time_global = current_time - start_time # Calculate how much time has passed since start

    minutes = int(elapsed_time_global // 60) # Convert elapsed seconds to minutes
    seconds = int(elapsed_time_global % 60) # Get remaining seconds after removing minutes

    time_display = f'{minutes}:{seconds:02d}' # time_display = f'{minutes:02d}:{seconds:02d}' == show time as 00:00

    time_entry.delete(0, tk.END) # Clear the time display entry box
    time_entry.insert(0, time_display) # Insert the formatted time at the beginning
    if tracker_active: # If tracking is still active
        time_after_id = window.after(1000, time_tracker) # Schedule this function to run again in 1 second
        return current_time # Return current time value


def pause_time():
    global tracker_active, time_after_id, elapsed_time_global, start_time
    tracker_active = False
    elapsed_time_global = time.time() - start_time
    window.after_cancel(time_after_id)

def resume_time():
    global tracker_active, start_time, elapsed_time_global
    tracker_active = True
    start_time = time.time() - elapsed_time_global
    time_tracker()



def stop_tracker():
    global tracker_active, time_display, time_after_id # Declare global variable to modify it
    tracker_active = False # Set tracking flag to inactive (stops the timer)
    time_display = "0:00" # Reset the time in the entry to be "0:00
    if time_after_id:
        window.after_cancel(time_after_id) # Used global variable for stopping the time_tracker before next iteration
        time_entry.delete(0, tk.END)
        time_entry.insert(0, time_display)





window = tk.Tk() # Create the main window
window.title('Reward System') # Set the window title to 'Reward System'

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3) # Create a frame with sunken border effect and 3-pixel border width
frm_form.pack() # Pack the frame into the window

labels = ['Time Elapsed:',
          'Total Points:',
          'Last App:',
          ]

# for idx, text in enumerate(labels):  #loop for the labels variable
time_label = tk.Label(master=frm_form, text=labels[0])  #Creating the labels from labels variable
time_entry = tk.Entry(master=frm_form, width=50)  #Creating entry displaying information
time_label.grid(row=0, column=0, sticky='e')
time_entry.grid(row=0, column=1)

points_label = tk.Label(master=frm_form, text=labels[1])  #Creating the labels from labels variable
points_entry = tk.Entry(master=frm_form, width=50)  #Creating entry displaying information
points_label.grid(row=1, column=0, sticky='e')
points_entry.grid(row=1, column=1)

last_app_label = tk.Label(master=frm_form, text=labels[2])  #Creating the labels from labels variable
last_app_entry = tk.Entry(master=frm_form, width=50)  #Creating entry displaying information
last_app_label.grid(row=2, column=0, sticky='e')
last_app_entry.grid(row=2, column=1)

buttons = ['Start log',
           'End log',
           'Pause log',
           'Resume log']

frm_buttons = tk.Frame()  # Frame for buttons
frm_buttons.pack(fill=tk.X, ipadx=10, ipady=10)

start_log_button = tk.Button(master=frm_buttons, text=buttons[0], command=start_time_tracking)  # button for start logging time
start_log_button.pack(side=tk.LEFT, ipadx=10)

pause_log_button = tk.Button(master=frm_buttons, text=buttons[2], command=pause_time) # pause the time
pause_log_button.pack(side=tk.LEFT, ipadx=10, padx=15)

resume_log_button = tk.Button(master=frm_buttons, text=buttons[3], command=resume_time) # resume the count
resume_log_button.pack(side=tk.LEFT, ipadx=10, padx=15)

end_log_button = tk.Button(master=frm_buttons, text=buttons[1], command=stop_tracker)  # button for end logging time
end_log_button.pack(side=tk.RIGHT, ipadx=10)

frm_active_program = tk.Frame(relief=tk.SUNKEN, width=3)  # Frame for tracking active program
frm_active_program.pack(fill=tk.X, ipadx=10, ipady=10)

active_program_label = tk.Label(master=frm_active_program, text=f'Active Program:')
active_program_label.pack(side=tk.LEFT)
active_program_entry = tk.Entry(master=frm_active_program, width=20)  # Entry for active program (shows which program
# is currently active
active_program_entry.pack(side=tk.LEFT)

if __name__ == '__main__':
    update_program_name()
    window.mainloop()
