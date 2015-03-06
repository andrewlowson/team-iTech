from django import forms
from fmk.models import Celebrity, Category, Game


class AddCelebrityForm (forms.ModelForm):
    first_name = forms.CharField(max_length=60, help_text="Enter the first name of the celebrity.")
    last_name = forms.CharField(max_length=60, help_text="Enter the last name of the celebrity.")
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        help_text="Assign a category to the celebrity."
    )

    class Meta:
        model = Celebrity
        fields = ('first_name', 'last_name', 'category', 'picture')


class AddCategoryForm (forms.ModelForm):
    name = forms.CharField(max_length=60, help_text="Enter the name of the category.")
    description = forms.CharField(
        widget=forms.Textarea,
        max_length=300,
        help_text="Enter a description of the category."
    )

    class Meta:
        model = Category
        fields = ('name', 'description')


class CreateGameForm (forms.ModelForm):
    celebrity1 = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        help_text="Select a celebrity."
    )
    celebrity2 = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        help_text="Select a celebrity."
    )
    celebrity3 = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        help_text="Select a celebrity."
    )

    class Meta:
        model = Game
        fields = ('celebrity1', 'celebrity2', 'celebrity3')