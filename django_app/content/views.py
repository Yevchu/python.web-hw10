from django.shortcuts import render, redirect, get_object_or_404

from .migrate_mongo_to_postrgres import feed_db
from .models import Tag, Author, Quote
from .forms import TagForm, QuoteForm

# Create your views here.
def main(request):
    print(feed_db())
    quotes = Quote.objects.all()
    return render(request, 'content/base.html', {'quotes': quotes})

def top_ten_tag(request):
    data = Tag.objects.all()
    unique_tag = []

    for tag in data:
        if tag in unique_tag:
            continue
        else:
            unique_tag.append(tag)
    
    return render(request, 'content/top_tags.html', {'tags': unique_tag[:10]})

def add_tag(request):
    if request.method == 'POST':
        form = TagForm(request.POST)
        if form.is_valid():
            data = form.data.get('tags')
            split_data = data.rstrip().split(' ')
            for el in split_data:
                tags_from_form = Tag(tags=el).save()
            return redirect(to='content:main')
        else:
            return render(request, 'content/add_tags.html', {'form': form})
    
    return render(request, 'content/add_tags.html', {'form': TagForm()})

def add_quote(request):
    tags = Tag.objects.all()

    if request.method == 'POST':
        form = QuoteForm(request.POST)
        if form.is_valid():
            new_quote = form.save()

            choice_tags = Tag.objects.filter(tags__in=request.POST.getlist('tags'))
            for tag in choice_tags.iterator():
                new_quote.tags.add(tag)
            
            return redirect(to='content:main')
        else:
            return render(request, 'content/add_quote.html', {'tags': tags, 'form': form})
    return render(request, 'content/add_quote.html', {'tags': tags, 'form': QuoteForm()})
