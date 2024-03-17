from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = '用户信息'  # 设置header
admin.site.site_title = '用户信息'   # 设置title
admin.site.index_title = '用户信息'
class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('username', 'enterprise_name', 'permission')  # 定义在列表视图中显示的字段

admin.site.register(user_info, UserInfoAdmin)

admin.site.register(App01BasicInfo)
