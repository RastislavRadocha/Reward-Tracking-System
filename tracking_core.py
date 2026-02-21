"""
tracking_core.py

Core computational logic for the Reward Tracking System.

This module contains pure functions responsible for:
- Elapsed time calculation
- Time block progression logic
- Points calculation

It does NOT:
- Interact with Tkinter
- Access or modify UI widgets
- Perform file I/O
- Perform network operations
- Maintain global state

All functions are deterministic and operate only on the
arguments provided to them.
"""

def calculate_points(points: int, last_block: int, current_block: int):
    # Calculates updated points based on time block progression
    # Points are only added when a new block is reached
    if current_block > last_block:
        points +=5
        last_block = current_block
    return points, last_block


def calculate_elapsed_global(current_time: int, start_time):
    elapsed_time = current_time - start_time
    return elapsed_time

def business_logic(start_time, current_time, points, last_block):
    if start_time == 0:
        return 0, points, last_block, "0:00"
    else:
        elapsed_time = calculate_elapsed_global(current_time,
                                                         start_time)  # Calculate how much time has
        # passed since the session started and store it in state
        current_block = int(elapsed_time) // 5  # Convert elapsed time into a discrete block index (used for point calculation)
        new_points, new_block = calculate_points(points, last_block, current_block)
        minutes = int(elapsed_time // 60)  # Convert elapsed seconds to minutes
        seconds = int(elapsed_time % 60)  # Get remaining seconds after removing minutes
        formatted_time = f"{minutes}:{seconds:02d}" # f'{minutes:02d}:{seconds:02d}' == show time as 00:00
        return elapsed_time, new_points, new_block, formatted_time