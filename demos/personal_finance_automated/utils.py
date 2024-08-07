from csv import reader
from settings import CSV_PATH

def all_transactions_budgeted(budgets, rules):
    categories = {"Misc":0}

    for line, transaction in enumerate(reader(open(CSV_PATH + "/demo.csv"))):
        if not line == 0:

            rule_match = False
            for rule in rules:
                rule['low_limit'] = float(rule['low_limit'])
                rule['upper_limit'] = float(rule['upper_limit'])

                if rule['low_limit'] >= float(transaction[2]) and rule['upper_limit'] <= float(transaction[2]) and (rule['text_match'] in transaction[1] or rule['text_match'] == '*'):
                    try:
                        categories[rule['category']] += abs(float(transaction[2]))
                    except KeyError as e:
                        categories[rule['category']] = abs(float(transaction[2]))
                    rule_match = True
                    break
            if rule_match == False:
                categories["Misc"] += float(transaction[2])

    for budget in budgets:
        try:
            categories[budget["name"]] = float(categories[budget["name"]])/float(budget["amount"])*100
        except KeyError as e:
            categories[budget["name"]] = 0

    return categories
