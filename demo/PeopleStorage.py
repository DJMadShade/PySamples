#!/usr/bin/env python

from main.MyMongo import MyMongo
from main.Person import Person
from test import GenerateTestData

GenerateTestData.populatePeople()

people = MyMongo("mongodb://localhost:27017", "PySamples", "People")

family = set(Person(**data) for data in people.getAll())

print("\nStored Records:\n\t%s" % '\n\t'.join(str(person) for person in family))
