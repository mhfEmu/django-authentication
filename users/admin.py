from django.contrib import admin
from .forms import CustomUserCreationForm, CustomUserChangeForm
from users.models import CustomUser

# Customize the admin site header and title
admin.site.site_header = 'Authentication Admin'
admin.site.site_title = 'Authentication Admin Panel'


class CustomUserAdmin(admin.ModelAdmin):
	add_form = CustomUserCreationForm
	form = CustomUserChangeForm
	list_display = ['username', 'email']
	
	
# Register your models here.
admin.site.register(CustomUser, CustomUserAdmin)
