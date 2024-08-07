from django.shortcuts import render
from django.conf import settings
from csv import reader
from io import StringIO
from .forms import CategoryBudgetFormSet, CategoryRuleFormSet
from .utils import all_transactions_budgeted
from settings import CSV_PATH

def personal_finance_automated(request):
    context = {}

    context["CSV"] = reader(open(CSV_PATH + "/demo.csv"))

    budget_forms = CategoryBudgetFormSet(
                                        initial = [
                                                    {"name": "Rent", "amount": 1400},
                                                    {"name": "Groceries", "amount": 400},
                                                    {"name": "Subscriptions", "amount": 100},
                                                    {"name": "Custom 1", "amount": 0},
                                                    {"name": "Custom 2", "amount": 100000},
                                                    {"name": "Custom 3", "amount": 500}
                                                ],
                                        prefix="budget"
                                        )
    context["category_budgets"] = budget_forms

    rule_forms = CategoryRuleFormSet(initial = [
                                                    {"category": "Rent", "low_limit": -15, "upper_limit":-100, "text_match":"*"},
                                                    {"category": "Rent", "low_limit": -15, "upper_limit":-100, "text_match":"*"},
                                                    {"category": "Rent", "low_limit": -15, "upper_limit":-100, "text_match":"*"},
                                                    {"category": "Rent", "low_limit": -15, "upper_limit":-100, "text_match":"*"},
                                                    {"category": "Rent", "low_limit": -15, "upper_limit":-100, "text_match":"*"},
                                                    {"category": "Rent", "low_limit": -15, "upper_limit":-100, "text_match":"*"},
                                                ],
                                    prefix='rule'
                                    )
    context["category_rules"] = rule_forms

    return render(request, "personal_finance_automated.html", context)

def recalculate(request):
    context = {}
    if request.method == "POST":
        # print(request.POST)
        budgets = CategoryBudgetFormSet(request.POST, prefix="budget")
        rules = CategoryRuleFormSet(request.POST, prefix='rule')

        if budgets.is_valid() and rules.is_valid():
            # print(budgets.cleaned_data)
            # print(rules.cleaned_data)
            actual_category_values = all_transactions_budgeted(budgets.cleaned_data, rules.cleaned_data)
            print(actual_category_values)
            context["categories"] = actual_category_values
        else:
            print(budgets.is_valid())
            print(rules.is_valid())

    return render(request, "test.html", context)