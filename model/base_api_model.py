from pydantic import BaseModel

class ApiBaseModel(BaseModel):
  @classmethod
  def read(cls, store, uuid):
    data = store.get(cls, uuid) 
    data["uuid"] = uuid
    return data

  @classmethod
  def recursive_read(cls, store, uuid):
    pass
    # from .klass import Klass

    # schema = cls.schema_json()
    # instance = store.get(cls, uuid)
    # x = json.loads(schema)
    # for key, definition in x["properties"].items():
    #   if "anyOf" in definition:
    #     any_of = definition["anyOf"]
    #     for any_of_item in any_of:
    #       if "$ref" in any_of_item:
    #         klass_str = any_of_item["$ref"].replace("#/definitions/", "")
    #         klass = Klass.get(klass_str)
    #         if instance[key] != None:
    #           instance[key] = klass.recursive_read(store, instance[key])
    #       elif "items" in any_of_item:
    #         if "$ref" in any_of_item["items"]:
    #           klass_str = any_of_item["items"]["$ref"].replace("#/definitions/", "")
    #           klass = Klass.get(klass_str)
    #           result = []
    #           for item in instance[key]:
    #             result.append(klass.recursive_read(store, item))
    #           instance[key] = result
    #   elif "$ref" in definition:
    #     klass_str = definition["$ref"].replace("#/definitions/", "")
    #     klass = Klass.get(klass_str)
    #     if instance[key] != None:
    #       instance[key] = klass.recursive_read(store, instance[key])
    # return instance

  @classmethod
  def list(cls, store):
    return store.list(cls)
  
  @classmethod
  def scope_reuse(cls):
    return True

  @classmethod
  def global_reuse(cls):
    return False