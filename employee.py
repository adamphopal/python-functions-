#Python Tutorial: Logging Advanced - Loggers, Handlers, and Formatters


import logging

#random change

logging.basicConfig(filename='employee.log', level=logging.INFO,
                    format='%(levelname)s:%(name)s:%(message)s')


class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - Email: {}'.format(self.fullname, self.email))

    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('hamim', 'phopal')
emp_2 = Employee('adam', 'phopal')
emp_3 = Employee('mike', 'black')
