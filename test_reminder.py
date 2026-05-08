import unittest
from reminder import Reminder
from exercise_manager import ExerciseManager
from logger import Logger

class TestReminder(unittest.TestCase):
    """Tests for the Reminder class."""

    def test_initial_interval(self):
        """Reminder should store the interval passed at creation."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        self.assertEqual(reminder.interval, 5)

    def test_update_interval(self):
        """Directly setting interval should update the value."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        reminder.interval = 10
        self.assertEqual(reminder.interval, 10)

    

    def test_is_valid_interval_positive(self):
        """A positive integer should be valid."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        self.assertTrue(reminder.is_valid_interval(10))

    def test_is_valid_interval_zero(self):
        """Zero should not be a valid interval."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        self.assertFalse(reminder.is_valid_interval(0))

    def test_is_valid_interval_negative(self):
        """A negative number should not be a valid interval."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        self.assertFalse(reminder.is_valid_interval(-1))

    def test_is_valid_interval_float(self):
        """A float should not be a valid interval."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        self.assertFalse(reminder.is_valid_interval(2.5))

    def test_is_valid_interval_string(self):
        """A string should not be a valid interval."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        self.assertFalse(reminder.is_valid_interval("5"))

    

    def test_set_interval_valid(self):
        """set_interval should update the interval for a valid value."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        reminder.set_interval(15)
        self.assertEqual(reminder.interval, 15)

    def test_set_interval_zero_raises(self):
        """set_interval should raise ValueError for zero."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        with self.assertRaises(ValueError):
            reminder.set_interval(0)

    def test_set_interval_negative_raises(self):
        """set_interval should raise ValueError for a negative number."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        with self.assertRaises(ValueError):
            reminder.set_interval(-3)

    def test_set_interval_float_raises(self):
        """set_interval should raise ValueError for a float."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        with self.assertRaises(ValueError):
            reminder.set_interval(2.5)

    def test_set_interval_string_raises(self):
        """set_interval should raise ValueError for a string."""
        reminder = Reminder(5, ExerciseManager(), Logger())
        with self.assertRaises(ValueError):
            reminder.set_interval("5")

if __name__ == "__main__":
    unittest.main()
