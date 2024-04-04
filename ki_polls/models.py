from django.db import models

class Question(models.Model):
    category = models.CharField(max_length=100)

    def __str__(self):
        return self.category

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=6, decimal_places=2)

    def __str__(self):
        return self.name

class KioskOrder(models.Model):
    kiosk_number = models.PositiveIntegerField(unique=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Kiosk Order - Number: {self.kiosk_number}"

class BeverageOrder(models.Model):
    kiosk_order = models.ForeignKey(KioskOrder, related_name='beverage_orders', on_delete=models.CASCADE)

    choice = models.ForeignKey(Choice, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0)
    ordered_at = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return "{} - Quantity: {}".format(self.choice.name, self.quantity)