# Just a small exercise with classes.
# In python console, do something like:
# >>> from dates import Date
# >>> today = Date(30,9,2019)
# >>> today.formdate()
# 30/09/2019

class Date:

    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    def formdate(self):
        print('{:02d}/{:02d}/{}'.format(self.day, self.month, self.year))
