from django.contrib import admin
from spartangear.models import Produto
# from .models import CustomUser

# class CustomUserAdmin(admin.ModelAdmin):
#     list_display = ('email',)

admin.site.register(Produto)