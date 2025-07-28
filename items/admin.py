from django.contrib import admin
from .models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'get_display_price')  # поля для отображения
    search_fields = ('name', 'description')  # поля для поиска
    list_filter = ('price',)  # фильтр

    def get_display_price(self, obj):
        return f"${obj.get_display_price()}"

    get_display_price.short_description = 'Price (USD)'