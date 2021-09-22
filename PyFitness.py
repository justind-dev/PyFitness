import json
from random import randrange,choice
from time import time, ctime, sleep

class ExerciseGenerator:
    def __init__(self) -> None:
        self.filename = 'exercises.json'
        self.exercises = None
        self.get_exercise_data()

    def get_exercise_data(self):
        with open(self.filename) as exercise_data:
            self.exercises = json.load(exercise_data)

    def get_random_exercise(self,level):
        random_exercise = choice(self.exercises)
        min = int(random_exercise["minimum"])
        max = int(random_exercise["maximum"])
        amount = self.get_count(min,max,level)
        return random_exercise["name"], random_exercise["metric"], amount

    def start_workout(self,type,intensity,number_of_exercises,workout_interval):
        if type == 1:
            self.turtle_school(workout_interval,number_of_exercises,intensity)
        elif type == 2:
            self.hyperbolic_time_chamber(intensity)
        pass

    def hyperbolic_time_chamber(self, intensity):
        ready = 'ready'
        while ready == 'ready':
            current_exercise = eg.get_random_exercise(intensity)
            print(f"You need to do {current_exercise[2]} {current_exercise[1]} of {current_exercise[0]} now.")
            ready = input("Enter 'ready' to get a new exercise! (anything else if you give up!)")
            
    def turtle_school(self,timer,number_of_exercises, intensity):
        while True:
            start_time = time()
            count = 1
            while count <= number_of_exercises:
                current_exercise = eg.get_random_exercise(intensity)
                print(f"You need to do {current_exercise[2]} {current_exercise[1]} of {current_exercise[0]} now!")
                count += 1
            print(f"Next workout at {ctime(start_time + timer)}")
            sleep(timer)
    
    def get_count(self, min, max, level):
        #Yajirobe 1-3% of max
        if level == 1:
            max = int(round(max * .03, 0))
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        #Yamcha 4-6%
        elif level == 2:
            max = int(round(max * .06, 0))
            min = round(max * .04, 0)
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        #Tien 7-10%
        elif level == 3:
            max = int(round(max * .10, 0))
            min = round(max * .07, 0)
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        #Krillin 11-15%
        elif level == 4:
            max = int(round(max * .15, 0))
            min = round(max * .11, 0)
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        #Goten 16-20%
        elif level == 5:
            max = int(round(max * .20, 0))
            min = round(max * .16, 0)
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        #Trunks 20-25%
        elif level == 6:
            max = int(round(max * .25, 0))
            min = round(max * .20, 0)
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        #Piccolo 26-35%
        elif level == 7:
            max = int(round(max * .35, 0))
            min = round(max * .26, 0)
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        #Gohan 36-50%
        elif level == 8:
            max = int(round(max * .50, 0))
            min = round(max * .36, 0)
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        #Vegeta 51-70%
        elif level == 9:
            max = int(round(max * .70, 0))
            min = round(max * .51, 0)
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        #Goku
        elif level == 10:
            max = int(round(max * 1, 0))
            min = round(max * .71, 0)
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        #Hidden level Jiren 125-200%
        elif level == 11:
            min = round(max * 1.25, 0)
            max = int(round(max * 2, 0))
            if max > 1:
                amount = randrange(min, max)
            else:
                amount = min
        if amount < 1:
            amount = 1
        return amount


if __name__ == "__main__":
    eg = ExerciseGenerator()
    intensity = 0
    type_of_workout = 0
    number_of_exercises = 0
    workout_interval = 0

    while intensity not in range(1,12):
        intensity = int(input("What intensity do you want to train at?\n\
        1  = Yajirobe\n\
        2  = Yamcha\n\
        3  = Tien\n\
        4  = Krillin\n\
        5  = Goten\n\
        6  = Trunks\n\
        7  = Piccolo\n\
        8  = Gohan\n\
        9  = Vegeta\n\
        10 = Goku\n\
        Your choice:"
        ))
        if intensity not in range(1,12):
            print("Sorry, thats not a valid intensity! Try again.")
    
    while type_of_workout not in range(1,3):
        type_of_workout = int(input("What type of workout do you want to do?\n\
        1  = Turtle School (You define training interval and how many exercises at each interval)\n\
        2  = Hyperbolic Time Chamber (You are prompted when you are ready for another workout)\n\
        Your choice? "))

        if type_of_workout == 1:
            print("Alright! Turtle School it is!")
            while workout_interval not in range(1,241):
                workout_interval = int(input("How often do you want a workout (minutes, 1-240)? "))*60
                if workout_interval not in range(1,241):
                    print("Sorry, thats not a valid range! Try again.")
            while number_of_exercises not in range(1,26):
                number_of_exercises = int(input("How many exercises do you want at each interval? (1-25)"))
                if number_of_exercises not in range(1,26):
                    print("Sorry, thats not a valid number of exercises! Try again.")
            eg.start_workout(type_of_workout, intensity, number_of_exercises, workout_interval)

        elif type_of_workout == 2:
            print("It feels like it never ends in the HTC, but lets do this!")
            workout_interval = 1
            number_of_exercises = 1
            eg.start_workout(type_of_workout, intensity, number_of_exercises, workout_interval)

        else:
            print("Sorry, thats not a valid type of workout! Try again.")