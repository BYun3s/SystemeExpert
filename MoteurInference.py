import json

class Fact:
    def __init__(self, name, value=False):
        self.name = name
        self.value = value

class Rule:
    def __init__(self, name, conditions, conclusion):
        self.name = name
        self.conditions = conditions
        self.conclusion = conclusion

class ExpertSystem:
    def __init__(self):
        self.facts = {}
        self.rules = {}
        self.potentiel_pannes = []

    def infer(self):
        self.load_data("data.json")
        self.load_fact("facts.json")
        inferred_facts = set()
        self.potentiel_pannes = []
        while True:
            added = False
            for rule_name, rule in self.rules.items():
                if rule_name not in inferred_facts:
                    conditions_met = all(self.facts[condition].value for condition in rule.conditions)
                    if conditions_met:
                        inferred_facts.add(rule_name)
                        self.facts[rule.conclusion] = Fact(rule.conclusion, True)
                        added = True
                        self.potentiel_pannes.append(rule.conclusion)
            if not added:
                break
  
    
    def load_data(self, filename):
        with open(filename, "r") as file:
            data = json.load(file)
            for fact_name, fact_value in data["facts"].items():
                self.facts[fact_name] = Fact(fact_name, fact_value)
            for rule_name, rule_data in data["rules"].items():
                self.rules[rule_name] = Rule(rule_name, rule_data["conditions"], rule_data["conclusion"])
    
    def load_fact(self, filename):
            with open(filename, "r") as file:
                data = json.load(file)
                for fact_name, fact_value in data["facts"].items():
                    self.facts[fact_name] = Fact(fact_name, fact_value)

# Créer une nouvelle instance de ExpertSystem


# Charger les faits et les règles depuis le fichier JSON
# expert_system.load_data()
