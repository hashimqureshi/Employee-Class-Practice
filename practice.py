class Employee:

    def __init__(self, first, last, pay, id):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.id  = id

    def fullname(self):
        return '{} {}'.format(self.first, self.last)

