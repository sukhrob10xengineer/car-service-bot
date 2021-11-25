from django.db import models


class UserModel(models.Model):
    USER_TYPE = (
        ("USER", "USER"),
        ("ADMIN", "ADMIN")
    )
    user_id = models.BigIntegerField(unique=True)
    name = models.CharField(max_length=300)
    user_type = models.CharField(max_length=300, choices=USER_TYPE)

    def __str__(self):
        return self.name


class Order(models.Model):
    servic_type = models.CharField(max_length=300)
    full_name = models.CharField(max_length=300)
    phone_num = models.CharField(max_length=300)
    car_name = models.CharField(max_length=300)
    cartime = models.CharField(max_length=300)
    payment = models.BooleanField(default=False)

    def __str__(self):
        return self.servic_type
