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
        if level ==1:
            random_exercise = choice(self.exercises)
            min = int(random_exercise["minimum"])
            max = int(random_exercise["maximum"])
            max = int(round(max*.25,0))
            amount = randrange(min,max)
        elif level == 2:
            random_exercise = choice(self.exercises)
            min = int(random_exercise["minimum"])
            max = int(random_exercise["maximum"])
            max = int(round(max*.50,0))
            min = round(max / 2,0)
            amount = randrange(min,max)
        elif level == 3:
            random_exercise = choice(self.exercises)
            min = int(random_exercise["minimum"])
            max = int(random_exercise["maximum"])
            max = int(max)
            min = round(max / 2,0)
            amount = randrange(min,max)

        return random_exercise["name"], amount

if __name__ == "__main__":
    eg = ExerciseGenerator()
    current_exercise = eg.get_random_exercise(2)
    print(f"You need to do {current_exercise[1]} {current_exercise[0]} now.")


