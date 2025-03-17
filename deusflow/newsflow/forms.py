from .models import Articles
from django.forms import ModelForm, TextInput, DateTimeInput, Textarea

class ArticleForm(ModelForm):
    class Meta:
        model = Articles
        fields = ['title','anons', 'full_text', 'date']

        widgets = {
            "title": TextInput(attrs={'class': 'form-control',
                                      "placeholder": 'Name of the title'}),
            "anons": TextInput(attrs={'class': 'form-control',
                                      "placeholder": 'Anons...'}),
            "full_text": Textarea(attrs={'class': 'form-control',
                                          "placeholder": 'Full Text...'}),
            "date": DateTimeInput(attrs={'class': 'form-control'}),
}