import unittest
from reminder import Reminder
from exercise_manager import ExerciseManager
from logger import Logger

class TestReminder(unittest.TestCase):

    def test_initial_interval(self):
        manager = ExerciseManager()
        logger = Logger()
        reminder = Reminder(5, manager, logger)
        self.assertEqual(reminder.interval, 5)

    def test_update_interval(self):
        manager = ExerciseManager()
        logger = Logger()
        reminder = Reminder(5, manager, logger)
        reminder.interval = 10
        self.assertEqual(reminder.interval, 10)

if __name__ == "__main__":
    unittest.main()

