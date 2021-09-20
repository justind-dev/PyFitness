import json
import os
from random import randrange,choice

class ExerciseGenerator:
    def __init__(self) -> None: 
        self.exercises = None
        self.get_exercise_data()

    def get_exercise_data(self):
        with open('exercises-simple.json') as exercise_data:
            self.exercises = json.load(exercise_data)

    def get_random_exercise(self,level):
        pass


if __name__ == "__main__":
    eg = ExerciseGenerator()
    for x in eg.exercises:
        print(x)

