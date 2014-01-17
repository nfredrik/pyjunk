import os
import json
JSONFILE='olle.json'

def load_json(file=JSONFILE):
    data = []
    if not os.path.exists(file):
        return data
    
    with open(file, 'rb') as fp:
        data = json.load(fp)
    return data


def save_json(data, file=JSONFILE):
    with open(file, 'wb') as fp:    
        json.dump(data, fp)