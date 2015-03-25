from django import forms
from fmk.models import Celebrity, Category, Game, Player, Result
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


# The form that is used to create a user account
class SignUpForm (forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        # Update the User model of the database
        model = User
        fields = ('username', 'email', 'password')

# The form that is used to take in the players choices of celebrities
# These will then be made into a game
class CreateGameForm (forms.ModelForm):
    celebrity1 = forms.ModelChoiceField(
        # Query all the celebrities in the database
        queryset=Celebrity.objects.all(),
        help_text="Select a celebrity."
    )
    celebrity2 = forms.ModelChoiceField(
        # Query all the celebrities in the database
        queryset=Celebrity.objects.all(),
        help_text="Select a celebrity."
    )
    celebrity3 = forms.ModelChoiceField(
        # Query all the celebrities in the database
        queryset=Celebrity.objects.all(),
        help_text="Select a celebrity."
    )


    class Meta:
        # The form populates the Game model in the database
        model = Game
        fields = ('celebrity1', 'celebrity2', 'celebrity3')

    # Method to validate each celebrity is used once in the form
    def clean(self):
        cleaned_data = super(CreateGameForm, self).clean()
        choice1 = cleaned_data.get('celebrity1')
        choice2 = cleaned_data.get('celebrity2')
        choice3 = cleaned_data.get('celebrity3')
        # Ensures that the celebrity choices that are made are all distinct
        # Error message displayed to the user
        msg = "Each celebrity can only be used once"
        # if all choice are identical
        if choice1 == choice2 and choice3 == choice2:
            # Add error messages to all the fields
            self.add_error('celebrity1', msg)
            self.add_error('celebrity2', msg)
            self.add_error('celebrity3', msg)
        # if the first and second choices are identical
        elif choice1 == choice2:
            # Add error messages to the first and second fields
            self.add_error('celebrity1', msg)
            self.add_error('celebrity2', msg)
        # if the second and third choices are identical
        elif choice2 == choice3:
            # add error messages to the second and third fields
            self.add_error('celebrity3', msg)
            self.add_error('celebrity2', msg)
        # if the first and third choices are identical
        elif choice1 == choice3:
            # add error messages to the first and third fields
            self.add_error('celebrity3', msg)
            self.add_error('celebrity1', msg)

# Takes in the choices that the player has made in a game either F, M or K
# This will be saved as a Result object with the appropriate Game id
class ResultForm (forms.ModelForm):

    result1 = forms.ChoiceField(
        # for each result field the user can select F,M or K
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
            ('K', 'Kill')]
    )


    class Meta:
        # form updates the Result model of the database
        model = Result
        fields = ('result1', 'result2', 'result3')
        exclude = ('game_id', 'player')

    def clean(self):
        cleaned_data = super(ResultForm, self).clean()
        choice1 = cleaned_data.get('result1')
        choice2 = cleaned_data.get('result2')
        choice3 = cleaned_data.get('result3')
        # Ensures that the player has selected one of each F, M and K
        # The error message is displayed to the user
        msg = "F,M and K can only be used once"
        # if all fields are identical
        if choice1 == choice2 and choice3 == choice2:
            self.add_error('result1', msg)
            self.add_error('result2', msg)
            self.add_error('result3', msg)
        # if the first and second choices are identical
        elif choice1 == choice2:
            self.add_error('result1', msg)
            self.add_error('result2', msg)
        # if the second and third choices match
        elif choice2 == choice3:
            self.add_error('result3', msg)
            self.add_error('result2', msg)
        # if the first and third selections match
        elif choice1 == choice3:
            self.add_error('result3', msg)
            self.add_error('result1', msg)

# Allows a registered player to add a celebrity to the game
# This is then stored as a celebrity object in the database
class AddCelebrityForm (forms.ModelForm):
    first_name = forms.CharField(max_length=60, help_text="Enter the first name of the celebrity.")
    last_name = forms.CharField(max_length=60, help_text="Enter the last name of the celebrity.")
    # category is a foreign key to the Category Model
    category = forms.ModelChoiceField(
        queryset=Category.objects.all(),
        help_text="Assign a category to the celebrity."
    )
    picture = forms.ImageField();

    class Meta:
        # form updates the Celebrity model of the database
        model = Celebrity
        fields = ('first_name', 'last_name', 'category', 'picture')


# Allows a registered player to add a celebrity category (Music/Film etc) to the game
# This is then stored as a Category object in the database
class AddCategoryForm (forms.ModelForm):
    name = forms.CharField(max_length=60, help_text="Enter the name of the category.")
    description = forms.CharField(
        widget=forms.Textarea,
        max_length=300,
        help_text="Enter a description of the category."
    )

    class Meta:
        # form updates the Category model of the database
        model = Category
        fields = ('name', 'description')
