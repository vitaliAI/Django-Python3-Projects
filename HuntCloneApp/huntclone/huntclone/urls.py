from django.contrib import admin
from django.urls import path, include

import products.views as product_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_views.home, name='home'),
    path('accounts/', include('accounts.urls') )
]
