from django import forms
from django.core.validators import MinLengthValidator, MaxLengthValidator
from datetime import date
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['image','title','director','genre','ratings','releaseDate','description']

        widgets={
            'image':forms.FileInput(attrs={'type':'file','class':'form-control','placeholder':'Image of Movie'}),
            'title':forms.TextInput(attrs={'type':'text', 'class':'form-control','placeholder':'Movie Title'}),
            'director':forms.TextInput(attrs={'class':'form-control','placeholder':'Director Name'}),
            'genre':forms.TextInput(attrs={'class':'form-control','placeholder':'Genre of Movie'}),
            'ratings':forms.NumberInput(attrs={'type':'number', 'class':'form-control','placeholder':'ratings of Movie', 'min':0, 'max':10}),
            'releaseDate':forms.DateInput(attrs={'type':'date', 'class':'form-control','placeholder':'Release Date'}),
            'description':forms.TextInput(attrs={'type':'text', 'class':'form-control','placeholder':'Description'}),

        }

    director=forms.CharField(validators=[MinLengthValidator(2),MaxLengthValidator(20)],widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Director Name'}))
    genre = forms.CharField(validators=[MaxLengthValidator(15)], widget=forms.TextInput(attrs={'class':'form-control','placeholder':'Genre of Movie'}))

    def clean_title(self):
        title = self.cleaned_data.get('title')
        if Movie.objects.filter(title=title).exists():
            raise forms.ValidationError('This title already exixts')
        return title
    
    def clean_releaseDate(self):
        releaseDate = self.cleaned_data.get('releaseDate')
        if releaseDate > date.today():
            raise forms.ValidationError('Release Date cannot be in future')
        return releaseDate




