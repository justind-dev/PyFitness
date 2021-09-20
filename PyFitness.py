import json
from random import randrange,choice
from time import time, ctime, sleep

class ExerciseGenerator:
    def __init__(self) -> None: 
        self.exercises = None
        self.get_exercise_data()

    def get_exercise_data(self):
        with open('exercises-simple.json') as exercise_data:
            self.exercises = json.load(exercise_data)

    def get_random_exercise(self,level):
        random_exercise = choice(self.exercises)
        min = int(random_exercise["minimum"])
        max = int(random_exercise["maximum"])
        amount = self.get_amount(min,max,level)
        return random_exercise["name"], amount

    def start_workout(self,timer,number_of_exercises, intensity):
        while True:
            start_time = time()
            count = 1
            while count <= number_of_exercises:
                current_exercise = eg.get_random_exercise(intensity)
                print(f"You need to do {current_exercise[1]} {current_exercise[0]} now.")
                count += 1
            print(f"Next workout at {ctime(start_time + timer)}")
            sleep(timer)
    
    def get_amount(self, min, max, level):
        if level ==1:
            max = int(round(max*.25,0))
            amount = randrange(min,max)
        elif level == 2:
            max = int(round(max*.50,0))
            min = round(max / 2,0)
            amount = randrange(min,max)
        elif level == 3:
            max = int(max)
            min = round(max / 2,0)
            amount = randrange(min,max)
        return amount


if __name__ == "__main__":
    eg = ExerciseGenerator()
    workout_interval = int(input("How often do you want a workout (minutes)? "))*60
    number_of_exercises = int(input("How many exercises do you want at each interval?"))
    intensity = int(input("What intensity do you want to train at?\n1 = beginner\n2=Intermediate\n3=Expert\nYour choice:"))
    eg.start_workout(workout_interval, number_of_exercises, intensity)




