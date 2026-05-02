from datetime import datetime

class Logger:
    def __init__(self, filename="mindfulness_log.txt"):
        self.filename = filename
        # Overwrite file at program start
        with open(self.filename, "w") as f:
            f.write("Mindfulness Log\n")
            f.write("====================\n\n")

    def log(self, exercise_message):
        """Append a completed exercise with timestamp."""
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        entry = f"{timestamp} — Completed: {exercise_message}\n"

        with open(self.filename, "a") as f:
            f.write(entry)
