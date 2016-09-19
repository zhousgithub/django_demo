from django.db import connection

cursor = connection.cursor()

from demo.cpws.models import User

user = User('asasas', 22)

user.save()