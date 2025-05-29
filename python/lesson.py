import time
import os
from user import User
import random
from datetime import date
from helper import Helper

COUNTDOWN = 2
LOW = 2  # lowest number available for practice
HIGH = 100  # highest number available for practice
M_LOW = -3  # lower bound for multiplication
M_HIGH = 12  # upper bound for multiplication
QUESTIONS = 2  # number of questions


class Lesson:
    """
    A lesson class with some tutorials and tests

    Methods:

    """

    def __init__(self, user: User):
        self.user = user
        self.helper = Helper()
        self.number = self.helper.get_number(LOW, HIGH, "Enter a number to practice:\t")
        self.times_table = [
            x for x in range(self.number * M_LOW, self.number * M_HIGH + 1, self.number)
        ]
        self.randoms: set[int] = set()
        self.fill_randoms()
        self.solutions = [x * self.number for x in self.randoms]
        self.answers: list[int] = []
        self.today = date.today().isoformat()

    def fill_randoms(self):
        while len(self.randoms) < QUESTIONS:
            self.randoms.add(random.randint(M_LOW, M_HIGH))

    def create_problems(self) -> User:
        for x in self.randoms:
            self.answers.append((int)(input(f"{x} times {self.number} =\t")))
        if self.solutions == self.answers:
            if not (
                self.today == self.user["last_login"]
                and self.today == self.info["today"]
            ):
                self.user["streak"] += 1
                self.user["last_login"] = self.today
                self.user["today"] = self.today
            else:
                self.info["last_login"] = self.today
        return self.info
