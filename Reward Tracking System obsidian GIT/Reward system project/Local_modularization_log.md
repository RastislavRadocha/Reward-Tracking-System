
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