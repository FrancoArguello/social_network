from users.models import Profile
from django import forms

class EditProfileForm(forms.ModelForm):
    
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={
            'class':'shadow-sm focus:ring-indigo-500 dark:bg-dark-third dark:text-dark-txt focus:border-indigo-500 block w-full sm:text-sm border-gray-300 rounded-md',
            })
    )
    picture = forms.ImageField(label='Profile Picture',required=False, widget=forms.FileInput)
    banner = forms.ImageField(label='Banner Picture',required=False, widget=forms.FileInput)
    location = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=25, required=False)
    url = forms.URLField(label='Website URL', widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=60, required=False)
    biography = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=260, required=False)
    studies =  forms.CharField(max_length=80)
    phone = location = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=25, required=False)
    occupation= location = forms.CharField(widget=forms.TextInput(attrs={'class': 'max-w-lg block w-full shadow-sm dark:bg-dark-third dark:text-dark-txt dark:border-dark-third focus:ring-indigo-500 focus:border-indigo-500 sm:max-w-xs sm:text-sm border-gray-300 rounded-md'}), max_length=25, required=False)
    
    
    class Meta:
        model = Profile
        fields = ('first_name','last_name','picture','banner','location','url','biography','studies','phone','occupation')