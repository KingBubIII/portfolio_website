from django import forms

class EmailContact(forms.Form):
    name = forms.CharField( required=True)
    email = forms.EmailField(required=True)
    budget = forms.ChoiceField(choices={"<$25": "<$25",
                                        "$25 - $75": "$25 - $75",
                                        "$100+": "$100+"},
                                required=True)
    message = forms.CharField(required=True)