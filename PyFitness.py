import json
import random
from statistics import mean


def load_json(filename):
    with open(filename) as data:
        return json.load(data)


class ExerciseImporter:
    def __init__(self, filename):
        self.exercises = load_json(filename)

    def get_exercises(self):
        return self.exercises


class Exercise:
    def __init__(self, **kwargs):
        self.name = kwargs["name"]
        self.metric = kwargs["metric"]
        self.minimum = int(kwargs["minimum"])
        self.maximum = int(kwargs["maximum"])
        self.mean = round(mean([self.minimum, self.maximum]))

    def get_metric(self):
        return self.metric

    def get_easy_count(self):
        count = self.minimum + random.randint(0, self.minimum)
        return count

    def get_medium_count(self):
        count = self.mean + random.randint(0, self.mean)
        return count

    def get_intense_count(self):
        count = self.maximum + random.randint(0, self.maximum)
        return count


if __name__ == "__main__":
    while True:
        exercises = ExerciseImporter("exercises.json")
        exercise = Exercise(**random.choice(exercises.get_exercises()))

        intensity = ""
        while intensity == "":
            intensity = input("How intense would you like your workout? (1,2,3) ")

        if intensity == "1":
            count = exercise.get_easy_count()
        elif intensity == "2":
            count = exercise.get_medium_count()
        elif intensity == "3":
            count = exercise.get_intense_count()
        else:
            print("INVALID ENTRY")
            count = 0

        if count > 0:
            print(f"Complete {count} {exercise.metric} of {exercise.name}")
