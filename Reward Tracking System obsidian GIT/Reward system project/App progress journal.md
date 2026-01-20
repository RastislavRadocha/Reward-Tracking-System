
# Session 1

After some time off this project, because i was studying AWS SAA, i had come back.
Before i had create simple UI from [[Reward system#^8f0338|first subpoint of phase 1]] , after that i had created a implemented functions such as `def time_tracker(), def stop_tracker(), def update_program_name(), def program_tracker()`, the functionality is pretty self-explanatory, however, it was working, it was lacking a kind of basic sense to it, for example:
- when i pressed the stop button, it did not reset the timer, it just stopped at that particular time, so basically it was paused
- it did not clear the window, did not insert any new value or anything like that
These basic logical steps must be present within the program and the function itself. They have been implemented now and any weird glitches are fixed, at least for the stop time function. Still a lot to do in phase one, and with the functions themselves.

Added also functioning `pause_time(), resume_time() and stop_tracker() functions` which was surprisingly not as hard as i have thought.

# Session 2

Added a point functionality, where every minute it will add 0.5 points to the points entry. It was done by using a global variable `points = 0.5` of type float, then i added a simple check to the `time_tracker()` function : `if int(elapsed_time_global) % 5 == 0 and elapsed_time_global > 0:  
    `points_entry.delete(0, tk.END)  
    `points_entry.insert(0, points)  
    `points = points + 0.5`
Since i already have the **pause and resume** logic tied to this function as well, the points are pausing and resuming automatically, only thing needed was to modify the stop function to delete and add the points again from 0. 

Also i have added a function to create a CSV files, and/or append existing data to it based on the last session. It has 3 columns `Time Elapsed, Total Points and Last App`, all of these are in a dictionary as keys, and the values are the respective values. However, now it tracks every program that is currently active, so that means whenever i press stop, i have to go the program itself, which will track itself, thus the last program tracked will always be the one i am writing. For the next session i have to implement a ignore check so that the app will be tracking itself, but other programs that are currently active.

# Session 3
After another long break, hopefully the last one, i come back and started thinking now about the points system, how is it stored, how is it read and used. For now i was only creating and/or appending data to a csv file, which is good, but i need to know how many points i earned per session and how many points i have in total, and also i want the app to know how many points in total i have. So, after some time i had updated the create_csv() function and added total_points_sum_csv() function to calculate all the points from previous session into one column,i have also reworked the points adding system, i have changed it to time blocks, where each passed block will add the selected amounts of points, and then divide it by then so that in will add decimal points into the csv, and it will also show decimal points in the app, not 10.15615234 second and it will round it up incorrectly. The setup for now is that every 5 second i get 0,5 points and that is exactly what is being shown and saved.

# Session 4

Today i will try to refactor one function to use parameters and create a different file where the UI will live. I do not want to over-engineer every step so i will do it slowly one by one, day by day. For the refactoring i am going to create a new git-branch, to clearly see the changes that were made, and later i am going to merge them into the main one.
- little update on the same topic, yesterday i refactored global variables `points, last_block`, to be used by a function which will calculate on which block the timer is, and how many points it should award.
- today i moved the global variables into a dictionary, and successfully updated the rest of the code which were still using the old  non-existent global variables, to be now read and written from and to the dictionary itself.
- After moving and refactoring 2 global variables (`Points`, `Last Block`), and create a new pure function for calculations points only, i did the same thing with the calculation of time:
```
	- def calculate_elapsed_global(current_time: int, start_time: int):  
    elapsed_time = current_time - start_time  
    return elapsed_time
    
state = {'Points': 0,  
         'Last Block': 0,  
         'Elapsed Time': 0}
         
def time_tracker():  # function for tracking time  
    global time_display, time_after_id  
    current_time = time.time() # Get current time  
    new_elapsed_time = calculate_elapsed_global(current_time, start_time)
  
    state['Elapsed Time'] = new_elapsed_time```

```


# Session 4.5

After last coding session, i have made more changes than intended, and i did not commit and push anything, so here i am going to list all changes that were made, and also commit this session with the software updates.
- Moved variable `start_time` in to the `state{}` dictionary
- Created `calculate_points(points, last_block, current_block)` function which takes care of modifying points on its own, instead of within `time_tracker()` function
- Created `calculate_elapsed_global(current_time, start_time)` function and refactored the `start_time` variable
- Moved `elapsed_time_global` variable into the `state{}` dictionary
- Fixed bug where the CSV file logged values like 177861945614, which were causing by wrong time calculation.
- Reordered logic inside `time_tracker()` function. 
	1. Schedule next tick
	2. Update elapsed time
	3. Calculate block index
	4. Calculate points
	5. Update state
	6. Update UI
- Resume function was setting the `state['Start Time']` variable, instead of resuming the time from Start function.
- Updated Pause function to store elapsed time into `state['Elapsed Time']`
- Updated Resume function to recalculate resumed time from `state['Elapsed Time']` and writes it into `state['Start Time']`
- `stop_tracker()` function now resets whole `state{}` dictionary
- Fixed UI point display presentation. (was showing integers, now it's showing floats)

- You refactored the app from “globals + mixed logic” into **state-driven, ordered, and guarded time + point tracking**, fixing async timing bugs and making Start, Pause, Resume, and Stop all behave correctly.
- Last big change was to Clean the old `start_time` global usage and refactored `time_tracker()` so time and points are calculated once per tick, instead of multiple times, and updated after block calculation.