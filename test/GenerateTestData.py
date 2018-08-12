from MyMongo import MyMongo
from Person import Person
from bson import ObjectId

people = MyMongo("mongodb://localhost:27017", "PySamples", "People")

people.delete({})

machuga = {
    Person("Sita", "Machuga", ObjectId('5b6f523193dda139c051a1f1')),
    Person("Jessica", "Machuga", ObjectId('5b6f524093dda139c051a1f2')),
    Person("James", "Machuga", ObjectId('5b6f524093dda139c051a1f3')),
    Person("Nathan", "Machuga", ObjectId('5b6f524093dda139c051a1f4')),
    Person("Isabella", "Machuga", ObjectId('5b6f524093dda139c051a1f5'))
}

ids = set(people.create(person._asdict()) for person in machuga)

print("Created people: %s" % ', '.join(str(id) for id in ids))
