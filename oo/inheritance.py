class LivingBeing:
    def say_hello(self):
        print('Hello')

    def say_world(self):
        print('World')

    def say_name(self):
        print('No name defined')


class Man(LivingBeing):
    def say_name(self):
        print('John Doe')
    # pass


class Women(LivingBeing):
    def say_name(self):
        print('Lara')
    # pass


# Mixin
class Printer:
    def __str__(self):
        self.say_hello()
        self.say_world()
        self.say_name()
        return ''


class Person(Man, Women, Printer):
    pass


# MRO - Method Resolution Order
# Python will look up for say_name method in the follow order:
# Person > Man > Women > LivingBeing
# The first class that implements this Method is Man
# so Man.say_name() is executed
obj = Person()
obj.say_name()

# Will execute Printer __str__ method
# that uses mixins to call self methods
print(obj)
