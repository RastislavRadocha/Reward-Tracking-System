import tkinter as tk
import time
import win32gui


def program_tracker():
    while True:
        current_program = win32gui.GetForegroundWindow()
        current_program_title = win32gui.GetWindowText(current_program)
        print(current_program_title)
        time.sleep(1)


window = tk.Tk()
window.title('Reward System')

frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
frm_form.pack()

labels = ['Time Elapsed:',
          'Total Points:',
          'Last App:',
          ]

for idx, text in enumerate(labels):  #loop for the labels variable
    label = tk.Label(master=frm_form, text=text)  #Creating the labels from labels variable
    entry = tk.Entry(master=frm_form, width=50)  #Creating entry displaying information
    label.grid(row=idx, column=0, sticky='e')
    entry.grid(row=idx, column=1)

buttons = ['Start log',
           'End log']

frm_buttons = tk.Frame()  # Frame for buttons
frm_buttons.pack(fill=tk.X, ipadx=10, ipady=10)

start_log_button = tk.Button(master=frm_buttons, text=buttons[0])  # button for start logging time
start_log_button.pack(side=tk.LEFT, ipadx=10)

end_log_button = tk.Button(master=frm_buttons, text=buttons[1])  # button for end logging time
end_log_button.pack(side=tk.RIGHT, ipadx=10)

frm_active_program = tk.Frame(relief=tk.SUNKEN, width=3)  # Frame for tracking active program
frm_active_program.pack(fill=tk.X, ipadx=10, ipady=10)

active_program_entry = tk.Entry(master=frm_active_program, width=20)  # Entry for active program (shows which program
# is currently active
active_program_entry.pack(side=tk.LEFT)

if __name__ == '__main__':
    window.mainloop()
    program_tracker()
