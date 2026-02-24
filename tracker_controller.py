import tracking_state
from session_model import create_session_snapshot
from storage_csv import create_csv
from cloud_sync import store_session_dynamodb
from tracking_core import business_logic
import time


def start_time_tracking():
    tracking_state.state['Tracking Active'] = True  # Set tracking flag to active
    tracking_state.state['Start Time'] = time.time()  # Record the current time as start time


def pause_time():
    tracking_state.state['Tracking Active'] = False
    tracking_state.state['Elapsed Time'] = time.time() - tracking_state.state['Start Time']


def resume_time():
    tracking_state.state['Tracking Active'] = True
    tracking_state.state['Start Time'] = time.time() - tracking_state.state['Elapsed Time']


def stop_tracker(user_id, last_program):
    if tracking_state.state['Elapsed Time'] == 0:
        return
    last_session = create_session_snapshot(user_id,
                                           tracking_state.state['Elapsed Time'],
                                           tracking_state.state['Points'],
                                           last_program)

    create_csv(last_session['duration_seconds'],
               last_session['points'],
               last_session['app_name'])

    tracking_state.last_session_data = last_session
    tracking_state.state['Tracking Active'] = False  # Set tracking flag to inactive (stops the timer)
    tracking_state.state['Points'] = 0
    tracking_state.state['Last Block'] = 0
    tracking_state.state['Elapsed Time'] = 0
    tracking_state.state['Start Time'] = 0

    return tracking_state.last_session_data


def update_tracking_tick(state, current_time):
    elapsed_time, new_points, new_block, formatted_time = business_logic(state['Start Time'],
                                                                         state['Points'],
                                                                         state['Last Block'],
                                                                         current_time)

    state['Elapsed Time'] = elapsed_time
    state['Points'] = new_points
    state['Last Block'] = new_block

    return formatted_time


def handle_storing_click():
    if store_session_dynamodb(tracking_state.last_session_data, api_key=API_KEY, api_url=API_URL):
        tracking_state.last_session_data = None
