import requests

def run_requests():
    response = requests.get('https://httpbin.org/get')
    return f'HTTP Status Code: {response.status_code}'
