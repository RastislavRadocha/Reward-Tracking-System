After some time off this project, because i was studying AWS SAA, i had come back.
Before i had create simple UI from [[Reward system#^8f0338|first subpoint of phase 1]] , after that i had created a implemented functions such as `def time_tracker(), def stop_tracker(), def update_program_name(), def program_tracker()`, the functionality is pretty self-explanatory, however, it was working, it was lacking a kind of basic sense to it, for example:
- when i pressed the stop button, it did not reset the timer, it just stopped at that particular time, so basically it was paused
- it did not clear the window, did not insert any new value or anything like that
These basic logical steps must be present within the program and the function itself. They have been implemented now and any weird glitches are fixed, at least for the stop time function. Still a lot to do in phase one, and with the functions themselves.

Added also functioning `pause_time(), resume_time() and stop_tracker() functions` which was surprisingly not as hard as i have thought.