from django.contrib import admin

from .models import Countries
from .models import Customer_info
from .models import Account_info
from .models import Transactions
from .models import Rules



admin.site.register(Countries)

admin.site.register(Customer_info)

admin.site.register(Account_info)

admin.site.register(Transactions)

admin.site.register(Rules)
