from department import Department


class Employee(Department):

    def __init__(self):
        Department.__init__(self,"IT")

    def __init__(self, first, last, pay, id):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay
        self.id  = id



    def fullname(self,Department):
        return '{} {}{}'.format(self.first, self.last,Department)




