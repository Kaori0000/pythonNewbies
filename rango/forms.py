from django import forms
from rango.models import Page, Category
from django.contrib.auth.models import User
from rango.models import UserProfile, Comment


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, 
                           help_text="Please enter the category name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):

    title = forms.CharField(max_length=128, 
                            help_text="Please enter the title of the page.")
    url = forms.URLField(max_length=200, 
                         help_text="Please enter the URL of the page.")
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url

        return cleaned_data

    class Meta:
        model = Page
        exclude = ('category',)



class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('name', 'body',)
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'body': forms.Textarea(attrs={'class': 'form-control'}),
        }
    

