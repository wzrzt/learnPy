
from Person import Person
a = Person(age=20, name='Tom', gender='male', height=1.65)
print('\n'.join(['%s:%s' % item for item in a.__dict__.items()]))
