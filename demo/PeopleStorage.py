from main.MyMongo import MyMongo
from main.Person import Person
from test.GenerateTestData import GenerateTestData

GenerateTestData.populatePeople()

people = MyMongo("mongodb://localhost:27017", "PySamples", "People")

family = set(Person(**data) for data in people.getAll())

print("\nStored Record:\n%s" % '\n'.join(str(person) for person in family))
