from typing import NamedTuple
from bson import ObjectId

class Person(NamedTuple):
    first: str
    last: str
    id: ObjectId = ObjectId()

    def __str__(self):
        return "%s %s" % (self.first, self.last)
