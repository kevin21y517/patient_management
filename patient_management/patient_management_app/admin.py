from django.contrib import admin
from .models import HStaff
# Register your models here.

class HStaffAdmin(admin.ModelAdmin):
    # 定义您希望在管理员中看到的字段
    list_display = ['username', 'password']

# 注册 HStaff 模型
admin.site.register(HStaff, HStaffAdmin)
