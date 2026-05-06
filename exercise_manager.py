import random
class ExerciseManager:
    """
    Stores/ manages mindfulness exercises.
    has customization and random selection.
    """

    def __init__(self):
        self.exercises = [
            "Take 3 deep breaths",
            "Stretch for 1 minute",
            "Relax your shoulders",
            "Close your eyes and breathe slowly",
            "Reflect on one thing you're grateful for"
        ]

    def add_exercise(self, exercise):
        """Adds a new exercise to the list."""
        self.exercises.append(exercise)

    def remove_exercise(self, exercise):
        """Removes an exercise if it exists."""
        if exercise in self.exercises:
            self.exercises.remove(exercise)

    def get_random_exercise(self):
        """Returns a random exercise."""
        return random.choice(self.exercises)

    def list_exercises(self):
        """Returns all exercises."""
        return self.exercises

