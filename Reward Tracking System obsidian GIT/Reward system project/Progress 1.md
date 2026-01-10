After some time off this project, because i was studying AWS SAA, i had come back.
Before i had create simple UI from [[Reward system#^8f0338|first subpoint of phase 1]] , after that i had created a implemented functions such as `def time_tracker(), def stop_tracker(), def update_program_name(), def program_tracker()`, the functionality is pretty self-explanatory, however, it was working, it was lacking a kind of basic sense to it, for example:
- when i pressed the stop button, it did not reset the timer, it just stopped at that particular time, so basically it was paused
- it did not clear the window, did not insert any new value or anything like that
These basic logical steps must be present within the program and the function itself. They have been implemented now and any weird glitches are fixed, at least for the stop time function. Still a lot to do in phase one, and with the functions themselves.

Added also functioning `pause_time(), resume_time() and stop_tracker() functions` which was surprisingly not as hard as i have thought.

# Progress 2

Added a point functionality, where every minute it will add 0.5 points to the points entry. It was done by using a global variable `points = 0.5` of type float, then i added a simple check to the `time_tracker()` function : `if int(elapsed_time_global) % 5 == 0 and elapsed_time_global > 0:  
    `points_entry.delete(0, tk.END)  
    `points_entry.insert(0, points)  
    `points = points + 0.5`
Since i already have the **pause and resume** logic tied to this function as well, the points are pausing and resuming automatically, only thing needed was to modify the stop function to delete and add the points again from 0. 

Also i have added a function to create a CSV files, and/or append existing data to it based on the last session. It has 3 columns `Time Elapsed, Total Points and Last App`, all of these are in a dictionary as keys, and the values are the respective values. However, now it tracks every program that is currently active, so that means whenever i press stop, i have to go the program itself, which will track itself, thus the last program tracked will always be the one i am writing. For the next session i have to implement a ignore check so that the app will be tracking itself, but other programs that are currently active.

# Progress 3
After another long break, hopefully the last one, i come back and started thinking now about the points system, how is it stored, how is it read and used. For now i was only creating and/or appending data to a csv file, which is good, but i need to know how many points i earned per session and how many points i have in total, and also i want the app to know how many points in total i have.