from django import forms
class FeedbackForm(forms.Form):
    name=forms.CharField(
        label="Enter your Name",
        widget = forms.TextInput(
            attrs = {
                'class':'form-control',
                'placeholder':'your name'
            }
        )
    )

    rating=forms.IntegerField(
        label = "Enter Your Rating",
        widget = forms.NumberInput(
            attrs = {
                'class':'form-control',
                'placeholder':'your rating'

            }
        )
    )

    feedback=forms.CharField(
        label = 'Enter Your Feedback',
        widget = forms.Textarea(
            attrs = {
                'class':'form-control',
                'placeholder':'your feedback'
            }
        )
    )