#!/usr/bin/env python3
import os
class Person:
    def __init__(self, name, weight, height):
        self.name = name
        self.weight = weight
        self.height = height
        self.bmi = 0.0

    def myfunc(self):
        gpt = 0
        bmi = 0.0
        bmi += float(weight) / float(height) **2
        print(f"Your Bmi is {round(bmi, 1)}")
        gpt = round(bmi, 1)
        command = f'tgpt -q "Hello My Name Is: {name}, and My BMI Is: {gpt} give me more details and give me some advices"'
        os.system(command)


name = input("What Is Your Name ? \n")
weight = input("What Is Your weight? \n")
height = input("What Is Your height by meter Like<1.8>? \n")

person_instance = Person(name, weight, height)
person_instance.myfunc()
