from django import forms
from todo.models import Tag, Task


class TagForm(forms.ModelForm):
    class Meta:
        model = Tag
        fields = "__all__"


class TaskForm(forms.ModelForm):
    tags = forms.ModelMultipleChoiceField(
        queryset=Tag.objects.all(),
        widget=forms.CheckboxSelectMultiple,
    )

    optional_deadline = forms.DateTimeField(
        required=False,
        label="",
        widget=forms.TextInput(attrs={"placeholder": "yyyy-mm-dd hr:m"})
    )

    class Meta:
        model = Task
        fields = ("content", "optional_deadline", "tags",)
