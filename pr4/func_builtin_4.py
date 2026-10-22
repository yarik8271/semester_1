import json

def run_json():
    data = {'lab': 4, 'status': 'completed'}
    return json.dumps(data)
