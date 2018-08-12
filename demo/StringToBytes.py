from MyMongo import MyMongo
from Person import Person
from bson import ObjectId

from .test import GenerateTestData

people = MyMongo("mongodb://localhost:27017", "PySamples", "People")

family = set(Person(**data) for data in people.getAll())

print("\nStored Record:\n%s" % '\n'.join(str(person) for person in family))
