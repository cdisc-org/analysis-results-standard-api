import json
from pydantic import BaseModel


class ApiBaseModel(BaseModel):
  @classmethod
  def read(cls, store, uuid):
    data = store.get(cls, uuid) 
    data["uuid"] = uuid
    return data

  @classmethod
  def recursive_read(cls, raw_json, uuid):
    from .klass import Klass
    print(cls)
    schema = cls.schema_json()
    instance = raw_json
    # print(instance)
    x = json.loads(schema)
    for key, definition in x["properties"].items():
      print(f"key = {key}, definition = {definition}")
      if "anyOf" in definition:
        any_of = definition["anyOf"]
        for any_of_item in any_of:
          if "$ref" in any_of_item:
            klass_str = any_of_item["$ref"].replace("#/definitions/", "")
            klass = Klass.get(klass_str)
            if instance[key] != None:
              instance[key] = klass.recursive_read(raw_json, instance[key])
          elif "items" in any_of_item:
            if "$ref" in any_of_item["items"]:
              klass_str = any_of_item["items"]["$ref"].replace("#/definitions/", "")
              klass = Klass.get(klass_str)
              result = []
              for item in instance[key]:
                result.append(klass.recursive_read(raw_json, item))
              instance[key] = result
      elif "$ref" in definition:
        klass_str = definition["$ref"].replace("#/definitions/", "")
        klass = Klass.get(klass_str)
        print(instance[key])
        if instance[key] != None:
          print("ping")
          instance[key] = klass.recursive_read(raw_json, instance[key])
    return instance

  @classmethod
  def list(cls, store):
    return store.list(cls)
  
  @classmethod
  def scope_reuse(cls):
    return True

  @classmethod
  def global_reuse(cls):
    return False