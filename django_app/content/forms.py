from django.forms import ModelForm, CharField, TextInput
from .models import Tag, Quote, Author

class AuthorForm(ModelForm):
    name = CharField(min_length=3, max_length=30, required=True, widget=TextInput)
    
    class Meta:
        model = Author
        fields = ['name']

class TagForm(ModelForm):

    tags = CharField(min_length=3, max_length=100, required=True, widget=TextInput)

    class Meta:
        model = Tag
        fields = ['tags']

class QuoteForm(ModelForm):

    author = AuthorForm()
    quote = CharField(min_length=3, max_length=180, required=True, widget=TextInput)

    class Meta:
        model = Quote
        fields = ['author', 'quote']
        exclude = ['tags']