from datetime import datetime
import faker
from random import randint, choice
import sqlite3

NUMBER_STUDENTS = 50
NUMBER_GROUPS = 4
NUMBER_SUBJECTS = 8
NUMBER_PROFS = 5
NUMBER_MARK = 5
MAX_MARKS = 3

NAME = "name"
SUBJECT = "subject"
NUMBER = "number"
MARK = "mark"

SUBJECTS = [
  "Mathematics", "Literature", "Geography", "Music", "Geometry", "Programming",
  "Lingustics", "History"
]


class DataGenerator:

  def __init__(self, number, item):

    self.number = number
    self.item = item
    self.fake = faker.Faker()

    self.dictionary = {
      NAME: self.fake.name,
      SUBJECT: self.subject_generator,
      NUMBER: self.group_generator,
      MARK: self.mark_generator
    }
    self.handler = self.dictionary[item]

  def subject_generator(self):
    return randint(1, NUMBER_SUBJECTS)

  def student_generator(self):
    return randint(1, NUMBER_STUDENTS)

  def proff_generator(self):
    return randint(1, NUMBER_PROFS)

  def group_generator(self):
    return randint(1, NUMBER_GROUPS)

  def mark_generator(self):
    return randint(3, NUMBER_MARK)

  # def subject_generator(self):
  #   return SUBJECTS[randint(0, len(SUBJECTS))]

  def generate(self):
    output = []
    for _ in range(self.number):
      output.append(self.handler())
    return output
