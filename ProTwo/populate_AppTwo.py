import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','ProTwo.settings')

import django
django.setup()

##fake scrpt
from AppTwo.models import User
from faker import Faker

fakegen = Faker()

#def add_User():
 #   U = User.objects.get_or_create()

def populate(N=5):

    for entry in range(N):
        fake_FirstName = fakegen.first_name()
        fake_LastName  = fakegen.last_name()
        fake_Email     = fakegen.email()

        U = User.objects.get_or_create(First_Name=fake_FirstName,Last_Name=fake_LastName,Email=fake_Email)[0]


if __name__ == '__main__':
    print('populating 3bad')
    populate(100)
    print("finish ")


