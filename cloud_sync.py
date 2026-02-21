import os
import requests


def cloud_sync(csv_path: str, api_url: str, api_key: str):
    # 1. Check file exists
    if not os.path.exists(csv_path):
        raise FileNotFoundError(f"CSV not found: {csv_path}")

    # 2. Send file to API
    with open(csv_path, "rb") as f:
        response = requests.post(
            f"{api_url}/sync",
            headers={
                "x-api-key": api_url
            },
            files={
                "file": f
            },
            timeout=10
        )

    # 3. Handle response
    if response.status_code == 200:
        return True
    else:
        raise RuntimeError(
            f"Cloud sync failed "
            f"(status={response.status_code}, body={response.text})"
        )


def cloud_sync_check(api_url, api_key):
    if os.path.exists('Study Logs/tracking_log.csv'):
        cloud_sync('Study Logs/tracking_log.csv', api_url=api_url, api_key=api_key)
        print('The file was uploaded successfully')
    else:
        print('The CSV does not exist')


def store_session_dynamodb(session_data, api_key, api_url):
    if session_data is None:
        print("Snapshot empty, nothing to store")
        return
    try:
        headers = {"x-api-key": api_key}
        response = requests.post(f"{api_url}/session", json=session_data, headers=headers, timeout=10)
        if response.status_code == 200:
            print(f"Session stored successfully (status={response.status_code})")
            return True
        else:
            print("Response:", response.text)
            return False
    except Exception as e:
        print("Request failed", e)
        return False