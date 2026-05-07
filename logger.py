import os
from datetime import datetime

#Create the logger class to helo the user track their goals/ needs
class Logger:
    def __init__(self, filename="mindfulness_log.txt"):
        self.filename = filename
        # Overwrite file at program start
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                f.write("Mindfulness Log\n")
                f.write("====================\n\n")

    def log(self, exercise_message):
        """Append a completed exercise with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} — Completed: {exercise_message}\n"

        with open(self.filename, "a") as f:
            f.write(entry)
