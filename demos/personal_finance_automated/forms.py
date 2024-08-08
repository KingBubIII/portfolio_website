from django import forms

class CategoryBudget(forms.Form):
    name = forms.CharField(widget=forms.TextInput(attrs={'readonly': 'readonly', "title":"This value is uneditable in this demo."}))
    amount = forms.DecimalField(widget=forms.TextInput(attrs={"title":"This is the max amout you would like to spend in the category. Overspending will cause the category bar to become red."}))
CategoryBudgetFormSet = forms.formset_factory(CategoryBudget, extra=0)

class CategoryRule(forms.Form):
    category = forms.ChoiceField(choices=(('Pick a Category', 'Pick a Category'),
                                            ('Personal', 'Personal'),
                                            ('Groceries', 'Groceries'),
                                            ('Subscriptions', 'Subscriptions'),
                                            ('Custom 1', 'Custom 1'),
                                            ('Custom 2', 'Custom 2'),
                                            ('Custom 3', 'Custom 3')),
                                widget=forms.Select(attrs={"title":"Select which category this rule will total to, therefore adding it's amount to the category spending bar."}),
                                required=False)
    low_limit = forms.DecimalField(widget=forms.TextInput(attrs={"title":"This limit is the minimum amount the transaction has to be for to be included in the rule."}),
                                    required=False)
    upper_limit = forms.DecimalField(widget=forms.TextInput(attrs={"title":"This limit is the maximum amount the transaction has to be for to be included in the rule."}),
                                    required=False)
    text_match = forms.CharField(widget=forms.TextInput(attrs={"title":"This searches the transaction description for the text entered here. Helps categorize transactions by company."}),
                                    required=False)
CategoryRuleFormSet = forms.formset_factory(CategoryRule, extra=0)