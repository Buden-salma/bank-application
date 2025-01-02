from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class Balance_table(models.Model):
    Account_type=models.CharField(max_length=50)
    Account_number=models.IntegerField(null=True,blank=True)
    balance=models.IntegerField(default=0)
    User_Id = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


    def __int__(self):
        return self.Account_number

class Transaction_history(models.Model):
    Customer_ID=models.ForeignKey(User, on_delete=models.CASCADE)
    Date_Time=models.DateTimeField(auto_now_add=True)
    Amount=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    E_Gift=models.BooleanField(default=False)
    Expenses=models.DecimalField(max_digits=10,decimal_places=2,null=True,blank=True)
    payee_ID=models.IntegerField()


    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['Customer_ID', 'payee_ID', 'Date_Time'],
                name='Customer_Transation_history'
            )
        ]

    def __str__(self):
        return f"Payment from {self.Customer_ID} to {self.payee_ID} on {self.Date_Time}"