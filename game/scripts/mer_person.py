# -*- coding: <UTF-8> -*-
from random import *
import renpy.store as store
import renpy.exports as renpy


class Person(object):

    def __init__(self):
        self.name = "Stranger"
        self.avatar = "images/ava/none.jpg"
        self.age = "adult"          # can be "child", "young", "adult" or "elder"
        self.gender = "male"        # can be "male", "female", "shemale" or "sexless"
        self.species = "human"      # "human", ???
        self.morphology = "humanoid"    # "humanoid", "centaur", "amorphous", "quadruped", "insectoid"
        self.alignment = ["Conformal", "Egoist"]  # Lawful-Conformal-Chaotic and Good-Egoist-Evil
        self.features = []
        self.ration = "full"        # can be  "none", "half", "full" or "double"
        self.chakra = 1             # Number of magic slots in one's soul
        self.sigil = None           # House sigil on the one's soul. Makes you able to use sparks directly
        self.sparks = 0             # Number of sparks in the soul
        self.inventory = []         # Possessed amd carried, but not worn items
        self.equipment = {}         # Slots for armor, cloth, weapon, jewelry, etc. One slot = one item
        self.lifestyle = 0         # Sparks spend each turn on a lifestyle
        self.skills = {
            "manual": 1,
            "oral": 1,
            "penetration": 1
        }
        self.members = ["Hands", "Mouth", "Butt"]   # Bodyparts to use as implements and more


    def attribute(self, attribute):
        """
        Evaluates base attribute value of person based on features, age, gender, etc.
        :param attribute: physique, agility, spirit or mind.
        :return: attribute value averege is 3, no less than 1
        """
        value = 3
        if self.age == "child":
            value -= 1
        if attribute == "physique" or attribute == "phy":
            if self.age == "adult":
                value += 1
            if self.gender == "male":
                value += 1
            elif self.gender == "female":
                value -= 1

        if attribute == "agility" or attribute == "agi":
            if self.age == "child":
                value += 1              # to be equally as high as adult and young
            elif self.age == "elder":
                value -= 1

        if attribute == "mind" or attribute == "mnd":
            if self.age == "elder":
                value += 1

        if value < 1:
            value = 1
        return value

    def hunger(self):
        hunger = self.attribute("physique")
        return hunger

    def food_consumed(self):
        if self.ration == "none":
            consumption = 0
        elif self.ration == "half":
            consumption = self.hunger()/2
            if consumption < 1:
                consumption = 1
        elif self.ration == "double":
            consumption = self.hunger()*2
        else:
            consumption = self.hunger()

        return consumption




