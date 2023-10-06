from .pymongo_db import client
from .models import Tag, Author, Quote

mongo_data = client['HomeWork9']

AUTHOR = mongo_data['author']
TAGS = mongo_data['tag']
QUOTES = mongo_data['quote']

def get_author(collection):

    author = collection.find()
    for el in author:
        feed_db = Author.objects.get_or_create(name=el['name'])
    return feed_db


def get_tag(collection):

    tags = collection.find()
    for el in tags:
        feed_db = Tag.objects.get_or_create(tags=el['tag'])
    return feed_db


def get_quote(collection):
    quotes = collection.find()
    for el in quotes:
        author = AUTHOR.find_one({'_id': el['author']})
        tags = TAGS.find_one({'_id': el['tags']})

        quote = Quote.objects.create(
            quote=el['quote'],
            author=Author.objects.get(name=author['name']) if author else Author.objects.get(name='Marilyn Monroe'),
        )
        if tags:
            tag, created = Tag.objects.get_or_create(tags=tags['tag'])
            quote.tags.set([tag])
        else:
            default_tag, created = Tag.objects.get_or_create(tags='love')
            quote.tags.set([default_tag])

    return 'Quotes imported successfully'

def feed_db():
    data = Quote.objects.first() and Author.objects.first() and Tag.objects.first()
    if data is None:
        get_author(AUTHOR)
        get_tag(TAGS)
        get_quote(QUOTES)
        return 'Done'
    else:
        return 'DB is already feed'
