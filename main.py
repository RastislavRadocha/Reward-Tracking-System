import csv
import datetime
import os.path
import tkinter as tk
import time
import pywinctl as pwc
import os
from datetime import datetime, timezone

import tracker_controller
from storage_csv import total_points_sum_csv
from tracking_core import business_logic
from cloud_sync import store_session_dynamodb, cloud_sync_check
import tracking_state

import requests

# import win32gui

# stale variables
CURRENT_USER_ID = "rastislav"
API_URL = os.getenv("API_URL")
API_KEY = os.getenv("API_KEY")


def program_tracker():
    current_program = pwc.getActiveWindow()
    if current_program is None:
        return ""

    current_program_title = current_program.title or ""  # Gets the window title
    # print(current_program_title)  # Testing print
    return current_program_title  # Return the title
    # current_program = win32gui.GetForegroundWindow()  # Gets the ID number of the window that is on top
    # current_program_title = win32gui.GetWindowText(current_program)  # Gets the name of the window/program/website page
    # print(current_program_title)  # Prints the title to console for testing purposes
    # return current_program_title  # returns the variable to actually use it


def update_program_name():  # function for updating the name in the TkInter window
    active_program = program_tracker()  # calls the program_tracker() function
    active_program_entry.delete(0, tk.END)  # delete everything at index 0 to the END
    active_program_entry.insert(0, active_program)  # reinsert the name of the program
    window.after(1000, update_program_name)  # repeat the function and sending it to the Tk.Inter window every second


# state = {'Points': 0,
#          'Last Block': 0,
#          'Elapsed Time': 0,
#          'Start Time': 0,
#          'Tracking Active': False}

last_program = ""


# last_session_data = None


def time_tracker():  # function for tracking time
    if tracking_state.state['Tracking Active']:  # If tracking is still active
        current_time = time.time()  # Get current time
        tracking_state.time_after_id = window.after(1000,
                                                    time_tracker)  # Schedule this function to run again in 1 second
        formatted_time = tracker_controller.update_tracking_tick(tracking_state.state, current_time)

        time_entry.delete(0, tk.END)  # Clear the time display entry box
        time_entry.insert(0, formatted_time)  # Insert the formatted time at the beginning

        points_entry.delete(0, tk.END)
        points_entry.insert(0, (tracking_state.state['Points'] / 10))


def ui_cleanup(last_program, stop_format_time):
    if tracking_state.time_after_id:
        window.after_cancel(
            tracking_state.time_after_id)  # Used global variable for stopping the time_tracker before next iteration
        time_entry.delete(0, tk.END)
        time_entry.insert(0, stop_format_time)
        points_entry.delete(0, tk.END)
        points_entry.insert(0, tracking_state.state['Points'])

        last_app_entry.delete(0, tk.END)
        last_app_entry.insert(0, last_program)
        total_points_entry = total_points_sum_csv()
        total_points_label_entry.delete(0, tk.END)
        total_points_label_entry.insert(0, total_points_entry)

    return last_program


def handle_storing_click():
    if store_session_dynamodb(tracking_state.last_session_data, api_key=API_KEY, api_url=API_URL):
        tracking_state.last_session_data = None


window = tk.Tk()  # Create the main window
window.title('Reward System')  # Set the window title to 'Reward System'


def handle_start():
    tracker_controller.start_time_tracking()
    time_tracker()


def handle_pause():
    tracker_controller.pause_time()
    if tracking_state.time_after_id:
        window.after_cancel(tracking_state.time_after_id)


def handle_resume():
    tracker_controller.resume_time()
    time_tracker()


def handle_stop():
    last_program = program_tracker()
    session = tracker_controller.stop_tracker(CURRENT_USER_ID, last_program)

    if tracking_state.time_after_id:
        window.after_cancel(tracking_state.time_after_id)

    if session:
        stop_format_time = "0:00"
        ui_cleanup(last_program, stop_format_time)


frm_form = tk.Frame(relief=tk.SUNKEN,
                    borderwidth=3)  # Create a frame with sunken border effect and 3-pixel border width
frm_form.pack()  # Pack the frame into the window

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

start_log_button = tk.Button(master=frm_buttons, text=buttons[0], command=handle_start)  # button for start logging time
start_log_button.pack(side=tk.LEFT, ipadx=10)

pause_log_button = tk.Button(master=frm_buttons, text=buttons[2], command=handle_pause)  # pause the time
pause_log_button.pack(side=tk.LEFT, ipadx=10, padx=15)

resume_log_button = tk.Button(master=frm_buttons, text=buttons[3], command=handle_resume)  # resume the count
resume_log_button.pack(side=tk.LEFT, ipadx=10, padx=15)

end_log_button = tk.Button(master=frm_buttons, text=buttons[1], command=handle_stop)  # button for end logging time
end_log_button.pack(side=tk.RIGHT, ipadx=10)

frm_cloud_button = tk.Frame()
frm_cloud_button.pack(fill=tk.X, ipadx=10, ipady=10)

cloud_sync_button = tk.Button(master=frm_cloud_button, text="Cloud Sync",
                              command=cloud_sync_check)
cloud_sync_button.pack(side=tk.LEFT, ipadx=5, ipady=3)

store_dynamodb_button = tk.Button(master=frm_cloud_button, text='Store DynamoDB',
                                  command=handle_storing_click)
store_dynamodb_button.pack(side=tk.RIGHT, ipadx=5, ipady=3)

frm_active_program = tk.Frame(relief=tk.SUNKEN, width=3)  # Frame for tracking active program
frm_active_program.pack(fill=tk.X, ipadx=10, ipady=10)

active_program_label = tk.Label(master=frm_active_program, text=f'Active Program:')
active_program_label.pack(side=tk.LEFT)
active_program_entry = tk.Entry(master=frm_active_program, width=20)  # Entry for active program (shows which program
# is currently active
active_program_entry.pack(side=tk.LEFT)

total_points_label = tk.Label(master=frm_active_program, text=f'Total Points:')
total_points_label.pack(side=tk.LEFT)
total_points_label_entry = tk.Entry(master=frm_active_program, width=5)
total_points_label_entry.pack(side=tk.LEFT)

if __name__ == '__main__':
    update_program_name()
    window.mainloop()
