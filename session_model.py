from datetime import timezone, datetime


def create_session_snapshot(user_id, duration_seconds, points, app_name):
    formatted_points = round(points / 10, 2)
    timestamp = datetime.now(timezone.utc).isoformat()
    return {"user_id": user_id,
            "duration_seconds": duration_seconds,
            "points": formatted_points,
            "app_name": app_name,
            "timestamp": timestamp
            }


