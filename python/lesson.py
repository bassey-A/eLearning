import time
import os
import random
from helper import Helper

COUNTDOWN = 2
LOW = 2         # lowest number available for practice
HIGH = 100      # highest number available for practice
M_LOW = -3      # lower bound for multiplication
M_HIGH = 12     # upper bound for multiplication
QUESTIONS = 2   # number of questions

class Lesson():
    """
    A lesson class with some tutorials and tests

    Methods:

    """
    def __init__(self, info):
        self.info = info
        self.helper = Helper()
        self.number = self.helper.get_number(LOW, HIGH, "Enter a number to practice:\t")
        self.times_table = [x for x in range(self.number * M_LOW, self.number * M_HIGH + 1, self.number)]
        self.randoms = set()
        self.fill_randoms()
        self.solutions = [x * self.number for x in self.randoms]
        self.answers = []

    def fill_randoms(self):
        while len(self.randoms) < QUESTIONS:
            self.randoms.add(random.randint(M_LOW, M_HIGH))

    def create_problems(self):
        for x in self.randoms:
            self.answers.append((int)(input(f'{x} times {self.number} =\t')))
        if self.solutions == self.answers:
            print(self.info)

    
    