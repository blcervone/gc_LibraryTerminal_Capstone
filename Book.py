# Your solution must include some kind of a book class with a title, author, status, condition
# and due date if checked out.
# Status should be On Shelf or Checked Out (or other statuses you can imagine).
# Condition will represent the wear and tear of the book,
# and will degrade each time the book is checked out. Use any data type you wish to repress this.
# If the book is too degraded, when it is returned it will be recycled.
from datetime import datetime, timedelta
import random as rand
class Book:
    def __init__(self, title, author, status, condition, due_date):
        self.title = title
        self.author = author
        self.status = status
        self.condition = condition
        self.due_date = due_date

    def set_due_date(self):
        self.due_date = (datetime.now()+timedelta(days=14)).strftime('%m-%d-%Y')

    def degrade(self):
        degrade_num=rand.randint(1, 5)
        self.condition -= degrade_num

    def __str__(self):
        return f'-\tTitle: {self.title}\n \tAuthor: {self.author}\n \tStatus: {self.status}'

