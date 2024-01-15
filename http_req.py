import requests
from datetime import datetime

def send_request(port, endpoint, method='GET', payload=None):
    url = f'http://localhost:{port}/{endpoint}'

    try:
        if method == 'GET':
            #print("in get")
            response = requests.get(url, json=payload)
            print(response)
        elif method == 'POST':
            #print("in post")
            #print(url, payload)
            response = requests.post(url, json=payload)
        elif method == 'PUT':
            response = requests.put(url, json=payload)
        elif method == 'DELETE':
            response = requests.delete(url, json=payload)
        else:
            raise ValueError(f"Unsupported HTTP method: {method}")

        #response.raise_for_status()  # Check if the request was successful
        print(response.text)
        return response
    except requests.exceptions.RequestException as e:
        print(f"Error: {e}")
        return None


uuid2 = send_request(7751, '/student/assignments', method='GET', payload={
    "X-Principal": {"user_id":1, "student_id":1}
}).json()['internalUUID']
