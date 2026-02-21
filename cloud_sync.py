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