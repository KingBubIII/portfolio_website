from django import forms

class CategoryBudget(forms.Form):
    name = forms.CharField(required=True)
    amount = forms.DecimalField(required=True)
CategoryBudgetFormSet = forms.formset_factory(CategoryBudget, extra=0)

class CategoryRule(forms.Form):
    category = forms.ChoiceField(choices=(('Rent', 'Rent'),
                                        ('Groceries', 'Groceries'),
                                        ('Subscriptions', 'Subscriptions'),
                                        ('Custom Category 1', 'Custom Category 1'),
                                        ('Custom Category 2', 'Custom Category 2'),
                                        ('Custom Category 3', 'Custom Category 3')),
                                required=True)
    low_limit = forms.DecimalField(required=True)
    upper_limit = forms.DecimalField(required=True)
    text_match = forms.CharField(required=True)
CategoryRuleFormSet = forms.formset_factory(CategoryRule, extra=0)