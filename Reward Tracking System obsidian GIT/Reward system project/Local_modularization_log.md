
### 21.02.2026

- After finishing Phase 2 Cloud integration [[Cloud_integration_log|Cloud Integration]], i have moved onto cleaning the internal structure of the app. Currently, the `main.py` file contains everything from UI logic, to calculating points, creating and writing into csv, time management etc. So, slowly i will move one or two functions, if the are coupled, together into separate files, update the functions with arguments, and make sure it is more readable. Everything without changing any internal logic.
	- The `create_csv()` and `total_points_sum_csv()` functions are coupled together, and are responsible for namely creating and updating csv with rows and columns specified, and calculating the points per session, but also across all the sessions. These two functions were moved into separate file `storage_csv.py`.
	- Since there is a new file, the functions cannot rely on the `state{}` dictionary with values, as well as on the global variables. To fix this, the `create_csv()` functions was rewritten with arguments, and the internal variables were adjusted to match the parameters.
	- The second function `total_points_sum_csv()` does not need any adjustments, it is not dependent on anything from `main.py` it simply checks if the file exists or no, then act accordingly
	- And of course, in order for these changes to be functional, i had to import the functions in the `main.py`.

- Next step was to kind of disassemble the `time_tracker()` function which was doing a multiple processes at once. First it was controlling UI elements, updating the UI entries with `window.after()` function, looping recursively and checking the state of the app itself. 
	- The goal is to separate business logic, UI logic, and calculation logic, so it becomes more clearer what the function is supposed to be doing.
	- Two functions have been moved, or rather the calculation logic of time, points, and time blocks into a separate file. This was documented in the first paragraph above, however i have created one more function `business_logic()` in the new `tracking_core.py` file, to which i rewrote the calculation functionality from `time_tracker()` in `main.py`.
	- It was using values from `state{}` dictionary, which was fine when it was referencing them inside `main.py`, however since the logic has been moved, i had to rewrote the function to be able to accept parameters.
	- Then in the `main.py`, i am doing 3 cycle phase cycle with said function. 
		- First, the function read core values from `state{}` dictionary in `main.py`. 
		- Then when calling the function, by passing the necessary arguments, it computes the values, and return new ones.
		- And lastly, i am re-assigning the new values to the `state{}` dictionary.
		- One more extra step, to update the formatted time within the UI

- Moreover, i created another file for modularization called `session_model.py` which server as a snapshot for the particular session. It builds a structured dictionary with key:pair values such as -> `id, points, elapsed time, app name, timestamp`. This data is later used for storing sessions on DynamoDB

### 22.02.2026

- Today i have created one more file for modularization, called `tracking_state.py`. It serves very simple purpose, holding variables, and the `state{}`, which were defined as global variables in the `main.py`. After moving the variables into a separate file, i had to update all the references inside the `main.py`, so for example:
	- `state['Points']` became `tracking_state.state['Points']` 
- This pattern was applied to every other global variable.
- If function was using this particular global variables, the global variable call at the top of the function was removed as well.

- Next step was to create a file which will handle the controls of the app - `start/pause/resume/stop` functions namely. The functions were already written in `main.py`, however it looked cluttered and since this is a modularization process, i wanted to have these separately. After moving these functions to separate file called `tracker_controller.py`, i also had to update the references to the `state{}` dictionary, as was stated above. Moreover, for the functionality, i wrote a wrapper functions inside the `main.py` for each of the function, with some adjustments, such as:
	- **start wrapper function** calls `start_time_tracking()`, and also `time_tracker()` to be able to update UI
	- **pause wrapper function** calls `pause_time()`, with a condition to not add another second before the next tick
	- **resume wrapper function** calls `resume_time()` and also call `time_tracker()` to keep updating the UI from the last time block
	- **stop wrapper function** it's a bit more complicated. At first it assign variable `last_program = program_tracker()`, to get the name of the last active window, then it will assign another variable `session` to the tracker controller **stop function**, which takes 2 argument (user_id and last_program), which server as a stop and reset. 2 Conditions are used, to stop the next tick, and to clean UI.

- After wrapping functions, and making the architecture increasingly modular, next step was to start cleaning some of the larger functions within `main.py`. The first one was `time_tracker()` which was basically doing everything at once, not so modular. It was checking if the **tracking state** is `True`, then what is the current time, scheduling the time ticks, calculations, assignment of new variables and mutating them, formatting the time string and updating UI. Simply said a mess. So after doing a bit of analyzing work, i have decided to split the function and move some of the functionality into other files which are mentioned above. Now `time_tracker()` does:
	- the scheduling
	- calling the controller layer
	- updating UI
- The interaction with the controller works as follows:
	- `time_tracker()` calls `update_tracking_tick(state, current_time)` and assign its return value to `formatted_time`.
	- `update_tracking_tick()` is not responsible for the calculation itself, instead it extracts the necessary values from `state{}` dictionary from another file, such as (`Start Time, Points, Last Block` together with `current_time`) and passes it to `business_logic()`
		- The `business_logic()` does not take variables as arguments, instead it receives required inputs, which then are calculated on and returned.
			- The returned values are unpacked, the domain-relevant values (`elapsed_time, new_points, new_block)` are written back into the `state{}` dictionary.
			- `formatted_time` is not stored in `state{}`, because it is used only to update UI.
			- The `state{}` dictionary contains more values, however not all of them are necessary for the calculations to be done, only the relevant one for time progression and point updates.
- From 7 responsibilities down to 2 only.
	- However, it still feels a bit heavy, especially with the UI updating. So the next step is going to be to take care of that.