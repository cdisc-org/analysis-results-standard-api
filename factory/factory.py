import model
import json


raw_json = None

def get_raw_data():
    global raw_json
    if raw_json == None:
        with open("./workfiles/examples/Sprint 12 Examples.json") as f:
            raw_json = json.load(f)
    return raw_json

def reporting_event_data():
    raw_json = get_raw_data()
    re = model.ReportingEvent.recursive_read(raw_json, 0)
    # print(re)

def method_data():
    raw_json = get_raw_data()
    return model.Method.recursive_read(raw_json, 0)

def method_data():
    raw_json = get_raw_data()
    return model.Method.recursive_read(raw_json, 0)
