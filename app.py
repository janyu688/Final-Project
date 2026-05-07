import flet as ft
from exercise_manager import ExerciseManager
from logger import Logger
from reminder import Reminder
import os

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

    # obj
    manager = ExerciseManager()
    logger = Logger()
    reminder = Reminder(5, manager, logger)
    current_exercise = {"value": None}
    output_text = ft.Text(value="", selectable=True)

    # app buttons
    def get_exercise(e):
        exercise = manager.get_random_exercise()
        current_exercise["value"] = exercise
        output_text.value = f"Try this: {exercise}"
        page.update()

    # SAME exercise the user saw
    def log_exercise(e):
        if current_exercise["value"] is not None:
            logger.log(current_exercise["value"])
            output_text.value = f"Logged: {current_exercise['value']}"
        else:
            output_text.value = "No exercise to log yet!"
        page.update()

    # show log
    def view_log(e):
        try:
            with open("mindfulness_log.txt", "r") as f:
                log_content = f.read()
        except FileNotFoundError:
            log_content = "No log file found yet."

        page.controls.clear()
        page.add(
            ft.ElevatedButton("Return to Menu", on_click=return_to_menu),
            ft.ElevatedButton("Clear Log", on_click=clear_log),            
            ft.Text(log_content, selectable=True)
        )
        page.update()

    # Return to main menu
    def return_to_menu(e):
        page.controls.clear()
        page.add(
            output_text,
            get_btn,
            log_btn,
            view_btn,
            clear_btn
        )
        output_text.value = "Welcome back! Choose an option."
        page.update()

    # wipes the log file clean
    def clear_log(e):
        with open("mindfulness_log.txt", "w") as f:
            f.write("Mindfulness Log\n")
            f.write("====================\n\n")
        output_text.value = "Log cleared!"
        page.update()

# More Buttons!
    get_btn = ft.ElevatedButton("Get Exercise", on_click=get_exercise)
    log_btn = ft.ElevatedButton("Log Exercise", on_click=log_exercise)
    view_btn = ft.ElevatedButton("View Log", on_click=view_log)
    clear_btn = ft.ElevatedButton("Clear Log", on_click=clear_log)

    # menu
    page.add(
        output_text,
        get_btn,
        log_btn,
        view_btn,
        clear_btn
    )
ft.app(target=main)
