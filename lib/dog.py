#!/usr/bin/env python3

# import ipdb
APPROVED_BREEDS = [
    "Mastiff",
    "Chihuahua",
    "Corgi",
    "Shar Pei",
    "Beagle",
    "French Bulldog",
    "Pug",
    "Pointer"
]


class Dog:
    def __init__(self, name="Leo", breed="Pug") -> None:
        self.name = name
        self.breed = breed

    @property
    def name(self):
        return self._name

    @name.getter
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if (isinstance(name, str) and 1 < len(name) < 25):
            self._name = name
            return
        else:
            print("Name must be string between 1 and 25 characters.")

    @property
    def breed(self):
        return self._breed

    @breed.getter
    def breed(self):
        return self._breed

    @breed.setter
    def breed(self, breed):
        if (breed not in APPROVED_BREEDS):
            print("Breed must be in list of approved breeds.")
        else:
            self._breed = breed
            return


# ipdb.set_trace()
