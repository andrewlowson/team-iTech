from django import forms
from fmk.models import Celebrity, Category, Game, Player, Result
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


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
        cleaned_data = super(CreateGameForm, self).clean()
        choice1 = cleaned_data.get('celebrity1')
        choice2 = cleaned_data.get('celebrity2')
        choice3 = cleaned_data.get('celebrity3')
        msg = "Each celebrity can only be used once"
        if choice1 == choice2 and choice3 == choice2:
            self.add_error('celebrity1', msg)
            self.add_error('celebrity2', msg)
            self.add_error('celebrity3', msg)
        elif choice1 == choice2:
            self.add_error('celebrity1', msg)
            self.add_error('celebrity2', msg)
        elif choice2 == choice3:
            self.add_error('celebrity3', msg)
            self.add_error('celebrity2', msg)
        elif choice1 == choice3:
            self.add_error('celebrity3', msg)
            self.add_error('celebrity1', msg)


class ResultForm (forms.ModelForm):

    result1 = forms.ChoiceField(
        choices= [('F', 'Fuck'),
            ('M', 'Marry'),
            ('K', 'KIll')]
    )
    result2 = forms.ChoiceField(
        choices=[('F', 'Fuck'),
            ('M', 'Marry'),
            ('K', 'KIll')]
    )
    result3 = forms.ChoiceField(
        choices=[('F', 'Fuck'),
            ('M', 'Marry'),
            ('K', 'KIll')]
    )


    class Meta:
        model = Result
        fields = ('result1', 'result2', 'result3')
        exclude = ('game_id', 'player')

    def clean(self):
        cleaned_data = super(ResultForm, self).clean()
        choice1 = cleaned_data.get('result1')
        choice2 = cleaned_data.get('result2')
        choice3 = cleaned_data.get('result3')
        msg = "F,M and K can only be used once"
        if choice1 == choice2 and choice3 == choice2:
            self.add_error('result1', msg)
            self.add_error('result2', msg)
            self.add_error('result3', msg)
        elif choice1 == choice2:
            self.add_error('result1', msg)
            self.add_error('result2', msg)
        elif choice2 == choice3:
            self.add_error('result3', msg)
            self.add_error('result2', msg)
        elif choice1 == choice3:
            self.add_error('result3', msg)
            self.add_error('result1', msg)

