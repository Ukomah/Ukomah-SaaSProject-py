from django import forms

from .models import Category, Link



class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        fields = ('name', )
        

class LinkForm(forms.ModelForm):
    """Form definition for MODELNAME."""

    class Meta:
        """Meta definition for MODELNAMEform."""
        model = Link
        fields = ('category','name','description', 'url')
