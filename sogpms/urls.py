from django.conf.urls import url, include
from .views import Dashboard, Register, Login, Logout, GetUserProfile, UserInfoUpdate, UserPassUpdate, BankList, AddBank, BankUpdate, BankDelete, AddAccount, AccountList, AccountUpdate, AccountDelete, AddCustomer, CustomerList, CustomerUpdate, CustomerDelete, AddPayment, PaymentList

urlpatterns = [
    url(r'^login$', Login, name='login'),
    url(r'^logout$', Logout, name='logout'),
    url(r'^register$', Register, name='register'),

    # User Related URLS
    url(r'^user/', include([
        url(r'^profile$', GetUserProfile, name='profile'),
        url(r'^profile/(?P<pk>\d+)$', UserInfoUpdate, name='user-info-update'),
        url(r'^profile/pass/(?P<pk>\d+)$', UserPassUpdate, name='user-pass-update'),
        # url(r'^edit/(?P<pk>\d+)$', UserInfoUpdate, name='user-info-update'),
    ])),

    url(r'^$', Dashboard, name='dashboard'),

    # Account Related URLS
    url(r'^account/', include([
        url(r'^$', AccountList, name='account-list'),
        url(r'^new$', AddAccount, name='add-account'),
        url(r'^edit/(?P<id>\d+)$', AccountUpdate, name='account-update'),
        url(r'^delete/(?P<id>\d+)$', AccountDelete, name='account-delete'),
    ])),

    # Customer Related URLS
    url(r'^customer/', include([
        url(r'^$', CustomerList, name='customer-list'),
        url(r'^new$', AddCustomer, name='add-customer'),
        url(r'^edit/(?P<id>\d+)$', CustomerUpdate, name='customer-update'),
        url(r'^delete/(?P<id>\d+)$', CustomerDelete, name='customer-delete'),
    ])),

    # Bank Related URLS
    url(r'^bank/', include([
        url(r'^$', BankList, name='bank-list'),
        url(r'^new$', AddBank, name='add-bank'),
        url(r'^edit/(?P<id>\d+)$', BankUpdate, name='bank-update'),
        url(r'^delete/(?P<id>\d+)$', BankDelete, name='bank-delete'),
    ])),

    # Payment Related URLS
    url(r'^payment/', include([
        url(r'^$', PaymentList, name='payment-list'),
        url(r'^new$', AddPayment, name='add-payment'),
    ])),
]