from django.contrib.auth.models import User
from django.db import models

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    user_address = models.CharField(max_length=250, blank=True, null= True)
    phone_no = models.CharField(max_length=25, blank=True, null= True)
    user_avatar = models.CharField(max_length=150, blank=True, null= True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username

    class Meta:
        db_table = 'user_profile'

class Account(models.Model):
    name = models.CharField(max_length=250)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'account'

class Bank(models.Model):
    name = models.CharField(max_length=250)
    branch_name = models.CharField(max_length=250)
    info = models.CharField(max_length=350)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name

    class Meta:
        db_table = 'bank'

class Customer(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(null=True, blank=True, max_length=200)
    contact_person = models.CharField(null=True, blank=True, max_length=200)
    phone_no = models.CharField(null=True, blank=True, max_length=20)
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'customer'

class Payment(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, blank=False, related_name='payment_customer')
    payment_date = models.DateTimeField(blank=False)
    payment_type = models.CharField(max_length=20, blank=False)
    cheque_number = models.CharField(max_length=50)
    cheque_of_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, blank=True, related_name='payment_cheque_bank')
    transaction_date = models.DateTimeField(blank=False)
    amount = models.DecimalField(max_digits=20, decimal_places=2)
    money_receipt_number = models.CharField(max_length=50)
    deposite_to_bank = models.ForeignKey(Bank, on_delete=models.CASCADE, blank=False, related_name='payment_deposit_bank')
    deposite_to_account = models.ForeignKey(Account, on_delete=models.CASCADE, blank=False, related_name='payment_deposit_account')
    deposite_date = models.DateTimeField(blank=False)
    attached_file = models.CharField(max_length=550, blank=True, null=True)
    is_deposited = models.CharField(max_length=10, default='Yes')
    is_deleted = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_created_by')
    updated_at = models.DateTimeField(auto_now=True)
    updated_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='payment_updated_by')

    class Meta:
        db_table = 'payment'