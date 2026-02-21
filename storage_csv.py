import csv
import os


""" Function for creating and/or appending new data into csv. file """
def create_csv(duration_seconds,  points, last_program):
    elapsed_time_converted = int(duration_seconds) # converted floats to integers so that in CSV file it will look
                                                    # clean
    points_rounded = points / 10

    total_points = total_points_sum_csv() + points_rounded

    csv_columns = {'Time Elapsed': elapsed_time_converted,
                   'Points per session': points_rounded,
                   'Last App': last_program,
                   'Total points': total_points}

    if not os.path.exists('Study Logs'):
        os.makedirs('Study Logs')
    if os.path.exists('Study Logs/tracking_log.csv'):
        with open('Study Logs/tracking_log.csv', mode='a') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(csv_columns.keys()))
            writer.writerow(csv_columns)
    else:
        with open('Study Logs/tracking_log.csv', mode='w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=list(csv_columns.keys()))
            writer.writeheader()
            writer.writerow(csv_columns)


def total_points_sum_csv():
    total = 0.0

    if not os.path.exists('Study Logs/tracking_log.csv'):
        return 0.0
    with open('Study Logs/tracking_log.csv', mode='r', newline='') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            try:
                total += float(row['Points per session'])
            except(KeyError, ValueError):
                continue

    return total