import flet as ft
from exercise_manager import ExerciseManager
from logger import Logger
from reminder import Reminder

def main(page: ft.Page):
    # Settings
    page.title = "Exercise Reminder App"
    page.theme_mode = "light"
    page.padding = 20

    page.bgcolor = ft.LinearGradient(
        begin="top",
        end="bottom",
        colors=["#E3F2FD", "#FFFFFF"]
    )

    # Obj
    manager = ExerciseManager()
    logger = Logger()
    reminder = Reminder(5, manager, logger)

    # Input/ Output
    interval_field = ft.TextField(
        label="Reminder interval (minutes)",
        value=str(reminder.interval),
        width=200,
    )

    output_text = ft.Text(value="", selectable=True)

    # Functions
    def set_interval(e):
        try:
            minutes = int(interval_field.value)
            reminder.interval = minutes
            output_text.value = f"Interval updated to {minutes} minutes."
        except ValueError:
            output_text.value = "Please enter a valid number."
        page.update()

    def get_exercise(e):
        exercise = manager.get_random_exercise()
        output_text.value = f"Try this: {exercise}"
        page.update()

    def log_exercise(e):
        exercise = manager.get_random_exercise()
        logger.log(exercise)
        output_text.value = f"Logged exercise: {exercise}"
        page.update()

    # App bar
    page.appbar = ft.AppBar(
        title=ft.Text("Exercise Reminder"),
        bgcolor="#2196F3",
        color="white"
    )

    # Buttons
    get_exercise_top_button = ft.ElevatedButton(
        content=ft.Text("Get Exercise", size=16, weight=ft.FontWeight.BOLD),
        bgcolor="#FF4081",
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=20,
        ),
        on_click=get_exercise
    )

    set_interval_button = ft.ElevatedButton(
        content=ft.Text("Set Interval", size=16, weight=ft.FontWeight.BOLD),
        bgcolor="#4CAF50",
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=20,
        ),
        on_click=set_interval
    )

    log_exercise_button = ft.ElevatedButton(
        content=ft.Text("Log Exercise", size=16, weight=ft.FontWeight.BOLD),
        bgcolor="#FF9800",
        color="white",
        style=ft.ButtonStyle(
            shape=ft.RoundedRectangleBorder(radius=12),
            padding=20,
        ),
        on_click=log_exercise
    )

    # main
    main_card = ft.Container(
        content=ft.Column(
            controls=[
                ft.Text("Exercise Reminder App", size=28, weight=ft.FontWeight.BOLD),
                get_exercise_top_button,
                interval_field,
                ft.Row(
                    controls=[
                        set_interval_button,
                        log_exercise_button,
                    ],
                    spacing=10,
                ),
                ft.Divider(),
                output_text,
            ],
            spacing=20,
        ),
        padding=30,
        bgcolor="white",
        border_radius=20,
        shadow=ft.BoxShadow(blur_radius=12, color="#00000030")
    )

    page.add(main_card)

if __name__ == "__main__":
    ft.app(target=main)

