from django.contrib import admin
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin # importing UserAdmin class. Sin already specified below as class so make alias BaseUserAdmin
from .forms import UserCreationForm
from .models import MyUser


class UserAdmin(BaseUserAdmin):
    #eveery time we add the user use the usercreationform
    add_form = UserCreationForm
    list_display = ('username','email','is_admin')
    list_filter = ('is_admin',)

    fieldsets = (
        (None, {'fields':('username','email','password')}),
         ('permissions',{'fields':('is_admin',)})

    )
    search_fields = ('username','email')
    ordering=('username','email')

    filter_horizontal = ()



admin.site.register(MyUser, UserAdmin)
# Register your models here.
admin.site.unregister(Group) # to get rid of default group
