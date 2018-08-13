import traceback
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.db import transaction
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.shortcuts import render
from pprint import pprint
from django.core.urlresolvers import reverse
from pms import settings
from .models import UserProfile, Bank, Account, Customer, Payment
from django.db.models.signals import post_save
from django.contrib.auth import authenticate, login, logout

def Register(request):
    if request.method == 'POST':
        if len(request.FILES) != 0:
            myfile = request.FILES['user_avatar']
            fs = FileSystemStorage(settings.USER_AVATAR_TARGET)
            filename = fs.save(myfile.name, myfile)
            avatar = '/static/img/' + fs.url(filename)
        else:
            avatar = '/static/img/no_img.png'
        try:
            with transaction.atomic():
                user = User.objects.create_user(
                    first_name=request.POST.get('first_name', None),
                    last_name = request.POST.get('last_name', None),
                    username = request.POST.get('username', None),
                    email=request.POST.get('email', None),
                    password=request.POST.get('password', None),
                    is_active= 0,
                )

                UserProfile.objects.create(
                    user=user,
                    user_address=request.POST.get('user_address', None),
                    phone_no=request.POST.get('phone_no', None),
                    user_avatar=avatar,
                )
                # return HttpResponseRedirect(reverse('login'))
                return JsonResponse({'success': True}, safe=False)
        except Exception:
            # traceback.print_exc()
            # return HttpResponseRedirect(reverse('register'))
            return JsonResponse({'error': True})
    else:
        return render(request, 'page/register.html')

def Login(request):
    if request.method == "GET":
        return render(request, 'page/login.html')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                return JsonResponse({'success': True}, safe=False)
        else:
            return JsonResponse({'error': True})


@login_required
def Logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))

@login_required
def GetUserProfile(request):
    return render(request, 'page/profile.html')

@login_required
def UserInfoUpdate(request, pk):
    if request.method == "POST":
        user = User.objects.get(id=pk)
        user_profile = UserProfile.objects.get(user_id=pk)
        if len(request.FILES) != 0:
            if request.FILES['user_avatar']:
                myfile = request.FILES['user_avatar']
                fs = FileSystemStorage(settings.USER_AVATAR_TARGET)
                filename = fs.save(myfile.name, myfile)
                avatar = '/static/img/' + fs.url(filename)
        else:
            avatar = user_profile.user_avatar
        try:
            user.first_name = request.POST.get('first_name', None)
            user.last_name = request.POST.get('last_name', None)
            user.save()

            user_profile.user_address = request.POST.get('user_address', None)
            user_profile.user_avatar = avatar
            user_profile.save()
            # messages.add_message(request, messages.SUCCESS, "Updated Client")
            return HttpResponseRedirect(reverse('profile'))
        except Exception:
            # traceback.print_exc()
            return HttpResponseRedirect(reverse('profile'))
            # messages.add_message(request, messages.WARNING, "Failed to Update Client")
    else:
        return render(request, 'page/profile.html')

@login_required
def UserPassUpdate(request, pk):
    if request.method == "POST":
        password = request.POST.get('password', None)
        user = User.objects.get(id=pk)
        user.set_password(password)
        user.save()
    return HttpResponseRedirect(reverse('dashboard'))
@login_required
def Dashboard(request):
    context = {
        'liactive': 1,
    }
    return render(request, 'page/index.html', context=context)

@login_required
def AccountList(request):
    account_list = Account.objects.filter(is_deleted=False)
    context = {
        'liactive': 2,
        'subliactive': 2.1,
        'accounts': account_list
    }
    return render(request, 'page/account/account-list.html', context=context)

@login_required
def AddAccount(request):
    if request.method == "POST":
        try:
            with transaction.atomic():
                Account.objects.create(
                    name=request.POST.get('name', None),
                    created_by = request.user
                )
                return JsonResponse({'success': True}, safe=False)
        except Exception:
            traceback.print_exc()
            return JsonResponse({'error': True})
    else:
        context = {
            'liactive': 2,
            'subliactive': 2.2,
        }
        return render(request, 'page/account/add-account.html', context=context)

@login_required
def AccountUpdate(request, id):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                account = Account.objects.get(id=id)
                account.name = request.POST.get('name', None)
                account.save()
                return JsonResponse({'success': True}, safe=False)
            except Exception:
                return JsonResponse({'error': True})

    else:
        if request.user.is_authenticated:
            account_list = Account.objects.get(id=id)
            context = {
                'liactive': 2,
                'account': account_list
            }
            return render(request, 'page/account/account-update.html', context=context)

@login_required
def AccountDelete(request, id):
    if request.user.is_authenticated:
        try:
            account = Account.objects.get(id=id)
            account.is_deleted = True
            account.save()
        except Exception:
            return HttpResponseRedirect(reverse('account-list'))
        return HttpResponseRedirect(reverse('account-list'))

@login_required
def BankList(request):
    bank_list = Bank.objects.filter(is_deleted=False)
    context = {
        'liactive': 3,
        'subliactive': 3.1,
        'banks': bank_list
    }
    return render(request, 'page/bank/bank-list.html', context=context)

@login_required
def AddBank(request):
    if request.method == "POST":
        try:
            with transaction.atomic():
                Bank.objects.create(
                    name=request.POST.get('name', None),
                    branch_name=request.POST.get('branch_name', None),
                    info=request.POST.get('info', None),
                    created_by=request.user
                )
                # return HttpResponseRedirect(reverse('bank-list'))
                return JsonResponse({'success': True}, safe=False)
        except Exception:
            traceback.print_exc()
            # return HttpResponseRedirect(reverse('create-bank'))
            return JsonResponse({'error': True})
    else:
        context = {
            'liactive': 3,
            'subliactive': 3.2,
        }
        return render(request, 'page/bank/add-bank.html', context=context)

@login_required
def BankUpdate(request, id):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                bank = Bank.objects.get(id=id)
                bank.name = request.POST.get('name', None)
                bank.branch_name = request.POST.get('branch_name', None)
                bank.info = request.POST.get('info', None)
                bank.save()
                return JsonResponse({'success': True}, safe=False)
            except Exception:
                return JsonResponse({'error': True})

    else:
        if request.user.is_authenticated:
            bank_list = Bank.objects.get(id=id)
            context = {
                'liactive': 3,
                'bank': bank_list
            }
            return render(request, 'page/bank/bank-update.html', context=context)

@login_required
def BankDelete(request, id):
    if request.user.is_authenticated:
        try:
            bank = Bank.objects.get(id=id)
            bank.is_deleted = True
            bank.save()
        except Exception:
            return HttpResponseRedirect(reverse('bank-list'))
        return HttpResponseRedirect(reverse('bank-list'))

@login_required
def CustomerList(request):
    customer_list = Customer.objects.filter(is_deleted=False)
    context = {
        'liactive': 4,
        'subliactive': 4.1,
        'customers': customer_list
    }
    return render(request, 'page/customer/customer-list.html', context=context)

@login_required
def AddCustomer(request):
    if request.method == "POST":
        try:
            with transaction.atomic():
                Customer.objects.create(
                    name=request.POST.get('name', None),
                    address=request.POST.get('address', None),
                    contact_person=request.POST.get('contact_person', None),
                    phone_no=request.POST.get('phone_no', None),
                    created_by=request.user
                )
                # return HttpResponseRedirect(reverse('client-list'))
                return JsonResponse({'success': True}, safe=False)
        except Exception:
            traceback.print_exc()
            # return HttpResponseRedirect(reverse('add-bank'))
            return JsonResponse({'error': True})
    else:
        context = {
            'liactive': 4,
            'subliactive': 4.2,
        }
        return render(request, 'page/customer/add-customer.html', context=context)

@login_required
def CustomerUpdate(request, id):
    if request.method == "POST":
        if request.user.is_authenticated:
            try:
                customer = Customer.objects.get(id=id)
                customer.name = request.POST.get('name', None)
                customer.address = request.POST.get('address', None)
                customer.contact_person = request.POST.get('contact_person', None)
                customer.phone_no = request.POST.get('phone_no', None)
                customer.save()
                return JsonResponse({'success': True}, safe=False)
            except Exception:
                return JsonResponse({'error': True})

    else:
        if request.user.is_authenticated:
            customer_list = Customer.objects.get(id=id)
            context = {
                'liactive': 4,
                'customer': customer_list
            }
            return render(request, 'page/customer/customer-update.html', context=context)

@login_required
def CustomerDelete(request, id):
    if request.user.is_authenticated:
        try:
            customer = Customer.objects.get(id=id)
            customer.is_deleted = True
            customer.save()
        except Exception:
            return HttpResponseRedirect(reverse('customer-list'))
        return HttpResponseRedirect(reverse('customer-list'))

@login_required
def PaymentList(request):
    payment_list = Payment.objects.all().select_related('customer').filter(is_deleted=False)
    from pprint import pprint
    pprint(payment_list)
    context = {
        'liactive': 5,
        'subliactive': 5.1,
        'payments': payment_list
    }
    return render(request, 'page/payment/payment-list.html', context=context)

@login_required
def AddPayment(request):
    if request.method == "POST":
        if len(request.FILES) != 0:
            if request.FILES['attached_file']:
                myfile = request.FILES['attached_file']
                fs = FileSystemStorage(settings.ATTACHMENT_FILE_TARGET)
                filename = fs.save(myfile.name, myfile)
                attached_file = '/static/attachments/' + fs.url(filename)
        else:
            attached_file = '/static/attachments/no_attachment.png'

        try:
            with transaction.atomic():
                Payment.objects.create(
                    customer_id=int(request.POST.get('customer', None)),
                    payment_date=request.POST.get('payment_date', None),
                    payment_type=request.POST.get('payment_type', None),
                    cheque_number=request.POST.get('cheque_number', None),
                    cheque_of_bank_id=int(request.POST.get('cheque_of_bank', None)),
                    transaction_date=request.POST.get('transaction_date', None),
                    amount=request.POST.get('amount', None),
                    money_receipt_number=request.POST.get('money_receipt_number', None),
                    deposite_to_bank_id=int(request.POST.get('deposite_to_bank', None)),
                    deposite_to_account_id=int(request.POST.get('deposite_to_account', None)),
                    deposite_date=request.POST.get('deposite_date', None),
                    attached_file=attached_file,
                    created_by = request.user,
                    updated_by_id = int(request.user.id)
                )
                # return HttpResponseRedirect(reverse('company'))
                return JsonResponse({'success': True}, safe=False)
        except Exception:
            traceback.print_exc()
            # return HttpResponseRedirect(reverse('add-payment'))
            return JsonResponse({'error': True})
    else:
        customer_list = Customer.objects.filter(is_deleted=False)
        bank_list = Bank.objects.filter(is_deleted=False)
        account_list = Account.objects.filter(is_deleted=False)
        context = {
            'liactive': 5,
            'subliactive': 5.2,
            'customers': customer_list,
            'banks': bank_list,
            'accounts': account_list
        }
        return render(request, 'page/payment/add-payment.html', context=context)