from django import forms
from fmk.models import Celebrity, Category, Game, Player, Result
from django.contrib.auth.models import User


class AddCelebrityForm (forms.ModelForm):
    first_name = forms.CharField(max_length=60, help_text="Enter the first name of the celebrity.")
    last_name = forms.CharField(max_length=60, help_text="Enter the last name of the celebrity.")
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        help_text="Assign a category to the celebrity."
    )
    picture = forms.ImageField();

    class Meta:
        model = Celebrity
        fields = ('first_name', 'last_name', 'category', 'picture')


class SignUpForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')


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
        queryset=Celebrity.objects.all(),
        help_text="Select a celebrity."
    )
    celebrity2 = forms.ModelChoiceField(
        queryset=Celebrity.objects.all(),
        help_text="Select a celebrity."
    )
    celebrity3 = forms.ModelChoiceField(
        queryset=Celebrity.objects.all(),
        help_text="Select a celebrity."
    )

    class Meta:
        model = Game
        fields = ('celebrity1', 'celebrity2', 'celebrity3')

    def clean(self):
        cleaned_data = self.cleaned_data
        celeb1 = cleaned_data.get('celebrity1')
        celeb2 = cleaned_data.get('celebrity2')
        celeb3 = cleaned_data.get('celebrity3')
        if celeb1 == celeb2 or celeb1 == celeb3 or celeb2 == celeb3:
            raise forms.ValidationError('Each celebrity can only be selected once')


class ResultForm (forms.ModelForm):

    OPTIONS = (
        ('F', 'Fuck'),
        ('M', 'Marry'),
        ('K', 'Kill'),
    )

    result1 = forms.ChoiceField(
        choices=OPTIONS
    )
    result2 = forms.ChoiceField(
        choices=OPTIONS
    )
    result3 = forms.ChoiceField(
        choices=OPTIONS
    )


    class Meta:
        model = Result
        fields = ('result1', 'result2', 'result3')
        exclude = ('game_id', 'player')

    def clean(self):
        cleaned_data = self.cleaned_data
        choice1 = cleaned_data.get('result1')
        choice2 = cleaned_data.get('result2')
        choice3 = cleaned_data.get('result3')
        if choice1 == choice2 or choice1 == choice3 or choice2 == choice3:
            raise forms.ValidationError('F,M and K can only be used once')