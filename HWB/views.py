from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

# Create your views here.
from HWB.models import Category, Banner, Artical, Tag, Link


def index(request):
    allcategory = Category.objects.all()
    # 查询幻灯片数据并切片
    banner = Banner.objects.filter(is_active=True)[0:4]
    # 推荐
    tui = Artical.objects.filter(tui_id=3)[:3]
    # 文章
    allarticle = Artical.objects.all().order_by('-id')[0:10]
    # 热门文章 通过浏览量进行推荐
    hot = Artical.objects.all().order_by('views')[0:10:-1]
    for h in hot:
        print(h.views)
    # 推荐文章
    remen = Artical.objects.filter(tui_id=2)[:6]
    # 标签
    tags = Tag.objects.all()
    # 友情链接
    links = Link.objects.all()
    return render(request, 'index.html', locals())


def list(request, lid):
    # 根据url中传进来的lid筛选文章
    list = Artical.objects.filter(category_id=lid)
    # 获取当前文章的分类的名字
    cname = Category.objects.get(id=lid)
    # 右侧栏的热门推荐 id=2热门推荐   id=3首页推荐
    remen = Artical.objects.filter(tui_id=2)[:6]
    # 分类列表
    allcategory = Category.objects.all()
    # 标签
    tags = Tag.objects.all()

    # 分页
    page = request.GET.get('page')
    # 5条数据进行分页
    paginator = Paginator(list, 5)
    try:
        # 获取当前页码记录
        list = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码输入不是整数，则显示第一页内容
        list = paginator.page(1)
    except EmptyPage:
        # 如果页码不在范围里，则显示最后一页的数据
        list = paginator.page(paginator.num_pages)
    return render(request, 'list.html', locals())
def show(request, sid):
    # 根据id查询文章
    show = Artical.objects.get(id=sid)
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    # 右侧栏的热门推荐 id=2热门推荐   id=3首页推荐
    remen = Artical.objects.filter(tui_id=2)[:6]
    # 随机推荐可能感兴趣的文章
    hot = Artical.objects.all().order_by('?')[:10]
    # 创建时间比此文章早的，并且同等分类的文章中的第一篇文章即为上一篇文章
    previous_blog = Artical.objects.filter(create_time__gt=show.create_time, category=show.category_id).first()
    # 创建时间比此文章晚的，并且同等分类的文章中的最后一篇文章即为上一篇文章
    next_blog = Artical.objects.filter(create_time__lt=show.create_time, category=show.category_id).last()
    # 点击后阅读量+1
    show.views = show.views +1
    show.save()
    return render(request, 'show.html', locals())

def tag(request, tag):
    # 通过标签筛选文章
    list = Artical.objects.filter(tags__name=tag)
    # 右侧栏的热门推荐 id=2热门推荐   id=3首页推荐
    remen = Artical.objects.filter(tui_id=2)[:6]
    # 获取所有的分类名、标签名
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    # print(tags)
    # 获取当前标签名
    now_name = Tag.objects.get(name=tag)
    # 分页处理
    # 分页
    page = request.GET.get('page')
    # 5条数据进行分页
    paginator = Paginator(list, 5)
    try:
        # 获取当前页码记录
        list = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码输入不是整数，则显示第一页内容
        list = paginator.page(1)
    except EmptyPage:
        # 如果页码不在范围里，则显示最后一页的数据
        list = paginator.page(paginator.num_pages)
    return render(request, 'tags.html', locals())



def search(request):
    # 获取搜索关键词,from表单提交
    ss = request.GET.get('search')
    # 关键字匹配 contains模糊查询，等价like '%值%'
    list = Artical.objects.filter(title__contains=ss)
    # print(list)
    # 右侧栏的热门推荐 id=2热门推荐   id=3首页推荐
    remen = Artical.objects.filter(tui_id=2)[:6]
    # 获取所有的分类名、标签名
    allcategory = Category.objects.all()
    tags = Tag.objects.all()
    # 分页处理
    # 分页
    page = request.GET.get('page')
    # 5条数据进行分页
    paginator = Paginator(list, 10)
    try:
        # 获取当前页码记录
        list = paginator.page(page)
    except PageNotAnInteger:
        # 如果页码输入不是整数，则显示第一页内容
        list = paginator.page(1)
    except EmptyPage:
        # 如果页码不在范围里，则显示最后一页的数据
        list = paginator.page(paginator.num_pages)
    return render(request, 'search.html', locals())
def about(request):
    allcategory = Category.objects.all()
    return render(request, 'page.html', locals())