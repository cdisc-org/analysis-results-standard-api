from fastapi import FastAPI, APIRouter
import uvicorn
import json

app = FastAPI(
        title="ARS API",
    )

ars_router = APIRouter(prefix="/mdr/ars") 

@ars_router.get("/packages/")
def get_all_ars_packages():
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return [data]
    

@ars_router.get("/packages/{package_id}/reportingevents/")
def get_all_package_reporting_events(package_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/reportingevents/{reportingevent_id}/")
def get_reporting_event(reportingevent_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/reportingevents/{reportingevent_id}/methods/")
def get_all_reportingevents_methods(reportingevent_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f).get("methods")
    return data
    

@ars_router.get("/methods/{method_id}/")
def get_method(method_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f).get("methods")[int(method_id)]
    return data
    

@ars_router.get("/methods/{method_id}/operations/")
def get_all_methods_operations(method_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/operations/{operation_id}/")
def get_operation(operation_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/operations/{operation_id}/refoprels/")
def get_all_operations_referenced_operation_relationship(operation_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/refoprels/{refoprel_id}/")
def get_referenced_operation_relationship(refoprel_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/reportingevents/{reportingevent_id}/analysissets/")
def get_all_reportingevents_analysissets(reportingevent_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/analysissets/{analysisset_id}/")
def get_analysisset(analysisset_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/reportingevents/{reportingevent_id}/analyses")
def get_all_reportingevents_analysis(reportingevent_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/analyses/{analysis_id}/")
def get_analysis(analysis_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/analyses/{analysis_id}/datagroupings/")
def get_all_analyses_datagrouping(analysis_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/datagroupings/{datagrouping_id}/")
def get__datagrouping(datagrouping_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data
    

@ars_router.get("/datagroupings/{datagrouping_id}/datagroups/")
def get_all_datagroupings_datagroup(datagrouping_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/reportingevents/{reportingevent_id}/datasubsets/")
def get_all_reportingevents_datasubset(reportingevent_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/datasubsets/{datasubset_id}/")
def get_datasubset(datasubset_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/reportingevents/{reportingevent_id}/analysisgroupings/")
def get_all_reportingevents_analysisgrouping(reportingevent_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/analysisgroupings/{analysisgrouping_id}/")
def get_analysisgrouping(analysisgrouping_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/analysisgroupings/{analysisgrouping_id}/analysisgroups/")
def get_all_analysisgrouping_analysisgroups(analysisgroup_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/analysisgroups/{analysisgroup_id}/")
def get_analysisgroup(analysisgroup_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/reportingevents/{reportingevent_id}/outputs/")
def get_all_reportingevents_output(reportingevent_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/outputs/{output_id}")
def get_output(output_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/outputs/{output_id}/displays/")
def get_all_outputs_display(output_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/displays/{display_id}/")
def get_display(display_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/reportingevents/{reportingevent_id}/categorizations/")
def get_all_reportingevents_categorization(reportingevent_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/categorizations/{categorization_id}/")
def get_categorization(categorization_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/categorizations/{categorization_id}/categories/")
def get_all_categorizations_category(categorization_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


@ars_router.get("/categories/{category_id}/")
def get_category(category_id_id):
    data = None
    with open("./workfiles/examples/Sprint 12 Examples.json") as f:
        data = json.load(f)
    return data


app.include_router(ars_router)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
