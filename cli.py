from reminder import Reminder
from exercise_manager import ExerciseManager
from logger import Logger

def main():
  """
  Entry point for the command-line interface
  creates an ExerciseManager, Logger, and Reminder, then runs an
  interactive menu loop that lets the user set the reminder interval,
  get a random exercise, or log a completed exercise.
  """
  manager = ExerciseManager()
  logger = Logger()

  # Keep prompting until the user enters a positive integer.
  while True:
    try:
      interval = int(input("Set initial reminder interval (minutes): "))
      if interval <= 0:
        raise ValueError
      break
    except ValueError:
      print("Please enter a positive whole number.")

  reminder = Reminder(interval, manager, logger)

  # main menu loop, runs until the user chooses to exit.
  while True:
    print("\n1. Set interval")
    print("2. Get exercise")
    print("3. Log exercise")
    print("4. Exit")

    choice = input("> ")

    if choice == "1":
      # Delegate validation to Reminder.set_interval so the rules stay in one place.
      try:
        new_interval = int(input("Minutes: "))
        reminder.set_interval(new_interval)
        print("Updated.")
      except ValueError:
        print("Please enter a positive whole number.")
    elif choice == "2":
      print(manager.get_random_exercise())
    elif choice == "3":
      # Pick an exercise, log it, then confirm to the user what was recorded.
      exercise = manager.get_random_exercise()
      logger.log(exercise)
      print("Logged:", exercise)
    elif choice == "4":
      break
    else:
      print("Invalid choice.")

if __name__ == "__main__":
    main()
