from django import forms
from file_system.models import Show_Files
from mptt.forms import TreeNodeChoiceField

class AddFilesForm(forms.Form):
    name = forms.CharField(max_length=40)
    parent = TreeNodeChoiceField(queryset=Show_Files.objects.all())
