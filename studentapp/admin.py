from django.contrib import admin
from studentapp.models import student

# Register your models here.

#第一種方法 -> 僅顯示名字
#admin.site.register(student)

#第二種方法 -> 顯示多個欄位
#加入ModelAdmin類別
#class studentAdmin(admin.ModelAdmin):
    #list_display = ('id', 'cName', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
#admin.site.register(student, studentAdmin)

#第三種方法 -> 顯示多個欄位、資料過濾、欄位搜尋、排序
class studentAdmin(admin.ModelAdmin):
    list_display = ('id', 'cName', 'cBirthday', 'cEmail', 'cPhone', 'cAddr')
    list_filter = ('cName', 'cSex')
    search_fields = ('cName', ) #需要','因為引數必須是list或tuple
    ordering = ('id', ) #需要','因為引數必須是list或tuple
admin.site.register(student, studentAdmin)