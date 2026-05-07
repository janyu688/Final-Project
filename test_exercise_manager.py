import unittest
from exercise_manager import ExerciseManager

# Now testto see if the exercises will execute
class TestExerciseManager(unittest.TestCase):

    def test_get_random_exercise_returns_string(self):
        manager = ExerciseManager()
        exercise = manager.get_random_exercise()
        self.assertIsInstance(exercise, str)

    def test_exercise_list_not_empty(self):
        manager = ExerciseManager()
        self.assertGreater(len(manager.exercises), 0)
# Call!
if __name__ == "__main__":
    unittest.main()

