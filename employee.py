class Employee:
    def get_hours(self):
        return 40
        # Works 40 hours / week.
    def get_salary(self):
        return 40000.0
    # $40,000.00 / year.
    def get_vacation_days(self):
        return 10
    # Two weeks' paid vacation.
    def get_vacation_form(self):
        return 'yello'


class Secretary(Employee):
    def print_message(self, text):
        print('Message of text: ', text)
