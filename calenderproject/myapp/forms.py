from django import forms
from django.contrib.admin.widgets import AdminDateWidget

class EntryForm(forms.Form):
    name = forms.CharField(max_length=50,
        widget=forms.TextInput(
            attrs={
                'style':'border-color:blue',
                'placeholder':'這裏填你 叫乜水?'
            }
        )
    )
    date = forms.DateField(widget=AdminDateWidget())
    
    description = forms.CharField(widget=forms.Textarea)
