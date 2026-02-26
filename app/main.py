class Person:
    people = {}

    def __init__(self, name: str, age: int) -> None:
        self.name = name
        self.age = age
        Person.people[name] = self


def create_person_list(people: list) -> list:
    person_list = []
    for persone in people:
        person_list.append(Person(persone["name"], persone["age"]))

    for i, persone in enumerate(people):
        instance = person_list[i]
        if persone.get("wife") is not None:
            instance.wife = Person.people[persone["wife"]]
        if persone.get("husband") is not None:
            instance.husband = Person.people[persone["husband"]]
    return person_list
