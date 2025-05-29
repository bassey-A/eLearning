# from crawler import DirectoryCrawler
from db_handler import DB_Handler
from user import User
from helper import Helper
import time

# from lesson import Lesson
import os
from datetime import date
import json


if __name__ == "__main__":
    print("Hello there!!!")
    name: str = input("Enter your name to get started: ")
    print(f"hej {name}. \nWelcome to another day of fun & learning!!!")
    handler = DB_Handler()
    logs: dict[str, dict[str, int | str]] | None = handler.read_local("streak.json")
    if name.casefold() in logs:  # type: ignore
        user = User(name, logs[name]["last_date"], logs[name]["streak"])  # type: ignore
    else:
        print(f"Glad to have you here {name.capitalize()}")
        user = User(name)

    print("Let's practice maths")
    help = Helper()
    choice: int = help.get_number(
        1, 2, "Enter 1 for multiplication\nEnter 2 for division"
    )
    
    # printf("My name is %s", "Adam")
    # printf("nums: %s, %s, %s", *range(1, 4))
    # help = Helper()
    # tttt = help.verbose(help.get_int)
    # age = tttt("Get age\t")
    # print(age)
