class Reminder:
  def __init__(self, message, interval):
    """Initialize reminder with message and interval in minutes."""
    self.message = message
    self.interval = interval
    self.running = False
  def is_valid_interval(self, minutes):
    """This program returns the minutes that are grader than 0"""
    return isinstance(minutes, int) and minutes > 0
  def set_interval(self, minutes):
    if not self.is_valid_interval(minutes):
      raise ValueError("Invalid interval")
    self.interval = minutes
  def load_interval(self, filename="interval.txt"):
    try:
      with open(filename, "r") as file:
        minutes = int(file.read().strip())
        if self.is_valid_interval(minutes):
          self.interval = minutes
        else:
          raise ValueError
except (FileNotFoundError, ValueError):
        print("Error loading interval.")
    
    
    
