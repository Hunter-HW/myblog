from django.contrib import admin
from .models import Category, Artical, Banner, Tag, Tui, Link


# Register your models here.

@admin.register(Artical)
class ArticalAdmin(admin.ModelAdmin):
    # 文章列表里显示想要显示的字段
    list_display = ('id', 'category', 'title', 'user', 'views', 'create_time')
    # 自动分页50条数据
    list_per_page = 50
    # 排序方式
    ordering = ('-create_time',)
    # 设置哪些字段可以进入编辑界面
    list_display_links = ('id', 'title')

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'index')

@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('id', 'text_info', 'img', 'link_url', 'is_active')

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Tui)
class TuiAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'link_url')