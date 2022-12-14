from django.shortcuts import get_object_or_404, render_to_response
from coltrane.models import Entry, Category

def entries_index(request):
    return render_to_response('coltrane/entry_index.html', {'entry_list': Entry.objects.all() })


def entry_detail(request, year, month, day, slug):
    import datetime, time
    date_stamp = time.strptime(year+month+day, "%Y%b%d")
    pub_date = datetime.date(*date_stamp[:3])
    entry = get_object_or_404(Entry, pub_date__year=pub_date.year, pub_date__month=pub_date.month, pub_date__day=pub_date.day, slug=slug)
    return render_to_response('coltrane/entry_detail.html', { 'entry': entry })

def category_list(request):
    return render_to_response('Coltrane/category_list.html', { 'object_list': Category.objects.all()})

def category_detail(request, slug):
    category = get_object_or_404(Category, slug=slug)
    return render_to_response('coltrane/category_detail.html', {
        'object_list': category.live.entry_set(),
    })


