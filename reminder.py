class Reminder:
  def __init__(self, message, interval):
    """Initialize reminder with message and interval in minutes."""
    self.message = message
    self.interval = interval
    self.running = False
  def is_valid_interval(self, minutes):
    return isinstance(minutes, int) and minutes > 0
  def set_interval(self, minutes):
    if not self.is_valid_interval(minutes):
      raise ValueError("Invalid interval")
    self.interval = minutes
    
