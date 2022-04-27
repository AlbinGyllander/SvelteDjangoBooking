from django.contrib import admin
from .models import Profile
from django.contrib.auth.models import User



from django.contrib.auth.admin import UserAdmin as BaseUserAdmin


# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class EmployeeInline(admin.StackedInline):
    model = Profile
    readonly_fields=('user',)

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (EmployeeInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)