from typing import Any, Dict
from pymongo import MongoClient


class MyMongo:
    class __MyClient:
        def __init__(self, uri: str, db: str, catalog: str):
            client = MongoClient(uri)
            db = client[db]
            self.catalog = db[catalog]

        def getAll(self, filterBy: Any = None) -> dict:
            return self.catalog.find(filterBy, {'_id': False})

        def findById(self, entityId: object) -> dict:
            return self.catalog.find_one({"id": entityId}, {'_id': False})

        def create(self, entity: dict):
            return self.catalog.insert_one(entity).inserted_id

        def update(self, entity: dict) -> None:
            self.catalog.update_one({"id": entity["id"]}, entity, True)

        def delete(self, filterBy: Any) -> None:
            self.catalog.delete_many(filterBy)

    __instances: Dict[str, __MyClient] = {}

    def __new__(cls, uri: str, db: str, catalog: str) -> __MyClient:
        params = "%s/%s.%s".format(uri, db, catalog)
        if params not in MyMongo.__instances.keys():
            MyMongo.__instances[params] = MyMongo.__MyClient(uri, db, catalog)
        return MyMongo.__instances[params]
