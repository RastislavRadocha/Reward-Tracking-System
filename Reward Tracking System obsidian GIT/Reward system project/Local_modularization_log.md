
### 21.02.2026

- After finishing Phase 2 Cloud integration [[Cloud_integration_log|Cloud Integration]], i have moved onto cleaning the internal structure of the app. Currently, the `main.py` file contains everything from UI logic, to calculating points, creating and writing into csv, time management etc. So, slowly i will move one or two functions, if the are coupled, together into separate files, update the functions with arguments, and make sure it is more readable. Everything without changing any internal logic.
	- The `create_csv()` and `total_points_sum_csv()` functions are coupled together, and are responsible for namely creating and updating csv with rows and columns specified, and calculating the points per session, but also across all the sessions. These two functions were moved into separate file `storage_csv.py`.
	- Since there is a new file, the functions cannot rely on the `state{}` dictionary with values, as well as on the global variables. To fix this, the `create_csv()` functions was rewritten with arguments, and the internal variables were adjusted to match the parameters.
	- The second function `total_points_sum_csv()` does not need any adjustments, it is not dependent on anything from `main.py` it simply checks if the file exists or no, then act accordingly
	- And of course, in order for these changes to be functional, i had to import the functions in the `main.py`.

- 