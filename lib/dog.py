#!/usr/bin/env python3

import ipdb

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
    def __init__(self, name="Fido", breed="Pug") -> None:
        self.name = name
        self.breed = breed

    def get_name(self):
        return self._name

    def set_name(self, name):
        if isinstance(name, str) and 0 < len(name) < 26:
            self._name = name
            return
        else:
            print("Name must be string between 1 and 25 characters.")

    def get_breed(self):
        return self._breed

    def set_breed(self, breed):
        if breed not in APPROVED_BREEDS:
            print("Breed must be in list of approved breeds.")
            return
        else:
            self._breed = breed
            return

    name = property(get_name, set_name)
    breed = property(get_breed, set_breed)


# ipdb.set_trace()
