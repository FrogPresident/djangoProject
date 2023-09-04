from django.contrib import admin
from .models import Transaction, Tag  # 引入你的模型

admin.site.register(Transaction)
admin.site.register(Tag)
