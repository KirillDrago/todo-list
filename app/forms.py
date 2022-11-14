from django import forms
from django.forms import DateTimeInput

from app.models import Task, Tag


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )
    deadline = forms.DateTimeField(
        widget=forms.SelectDateWidget,
        required=False
    )

    class Meta:
        model = Task
        fields = "__all__"
