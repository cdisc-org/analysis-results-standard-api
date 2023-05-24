from model.analysis import Analysis
from model.analysis_categorization import AnalysisCategorization
from model.analysis_method import AnalysisMethod
from model.analysis_set import AnalysisSet
from model.data_subset import DataSubset
from model.display_sections import DisplaySection
from model.method import Method
from model.nested_list import NestedList
from model.output import Output
from model.reporting_event import ReportingEvent
from model.subject_grouping_factor import SubjectGroupingFactor

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
    re = ReportingEvent.recursive_read(raw_json, 0)
    # print(re)

def method_data():
    raw_json = get_raw_data()
    return Method.recursive_read(raw_json, 0)

def method_data():
    raw_json = get_raw_data()
    return Method.recursive_read(raw_json, 0)
