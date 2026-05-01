from reminder import Reminder
from exercise_manager import ExerciseManager
from logger import Logger

def main():
  remainder = Remainder("Stay mindful", 5)
  manager = ExerciseManager()
  logger = Logger()

while True:
  print("\n1. Set interval")
  print("\n1. Set interval")
  print("\n1. Set interval")
  print("\n1. Set interval")

choice = input("> ")

if choice == "1":
  remainder.set_interval(int(input("Minutes: ")))
  print("Updated.")
elif choice == "2":
  print(manager.get_exercise())
elif choice == "3":
  logger.log("Exercise completed")
elif choice == "4":
  break
if__name__ == "__main__":
     main()
