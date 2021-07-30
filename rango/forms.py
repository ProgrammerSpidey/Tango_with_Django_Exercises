from django import forms
from rango.models import Page, Category, UserProfile
from django.contrib.auth.models import User

# Let User to use/full Form cloud be effcient to collect information

class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the category name.")

    # IntegerField: Visting times & liking times
    views = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
    # initial = 0 : users or visitors cannot change this value
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial = 0)
    slug = forms.CharField(widget=forms.HiddenInput(), required = False)

    # a inline class to provide additional information on the form
    class Meta:
        model = Category
        fields = ('name',)

class PageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the title of the page.")

    url = forms.URLField(max_length=200, help_text="Please enter the URL of the page.")

    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        # association between the ModelForm and a model
        model = Page
        exclude = ('category',)
    
    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')
        # fields = {'title','url','views'}

        # if behind the url is null, add http://
        if url and not url.startswith('http://'):
            url = f'http://{url}'
            cleaned_data['url'] = url
        
        return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)