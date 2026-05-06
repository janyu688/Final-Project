from reminder import Reminder
from exercise_manager import ExerciseManager
from logger import Logger

def main():
  manager = ExerciseManager()
  logger = Logger()
  interval = int(input("Set initial reminder interval (minutes): "))
  reminder = Reminder(interval, manager, logger)

  while True:
    print("\n1. Set interval")
    print("2. Get exercise")
    print("3. Log exercise")
    print("4. Exit")

    choice = input("> ")

    if choice == "1":
      new_interval = int(input("Minutes: "))
      reminder.interval = new_interval * 60
      print("Updated.")
    elif choice == "2":
      print(manager.get_random_exercise())
    elif choice == "3":
      exercise = manager.get_random_exercise()
      logger.log(exercise)
      print("Logged:", exercise)
    elif choice == "4":
      break
    else:
      print("Invalid choice.")
if __name__ == "__main__":
    main()
