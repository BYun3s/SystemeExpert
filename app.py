from flask import Flask, render_template, request, redirect, url_for
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required

from MInf import *
import json

app = Flask(__name__)

expert_system = ExpertSystem()

app.secret_key = 'S' 
login_manager = LoginManager()
login_manager.init_app(app)

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = ''

class User(UserMixin):
    pass

@login_manager.user_loader
def load_user(user_id):
    if user_id == ADMIN_USERNAME:
        user = User()
        user.id = ADMIN_USERNAME
        return user
    else:
        return None

def read_json():
    with open('data.json', 'r') as file:
        data = json.load(file)
    facts = data.get('facts', {})
    rules = data.get('rules', {})
    return data, facts, rules

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            user = User()
            user.id = ADMIN_USERNAME
            login_user(user)
            return redirect(url_for('admin'))
    return render_template('login.html')

@login_manager.unauthorized_handler
def unauthorized_callback():
    return redirect(url_for('login'))

@app.route('/logout', methods=['POST'])
def logout():
    logout_user()
    return redirect(url_for('accueil'))

@app.route('/admin')
@login_required
def admin():
    
    return render_template('admin.html', facts=facts, rules=rules)

@app.route('/')
def accueil():
    
    return render_template('accueil.html', facts=facts)

@app.route('/resultat', methods=['POST'])
def resultat():
    if request.method == 'POST':
        selected_facts = request.form.getlist('facts')
        facts_states = {"facts": {fact: True for fact in selected_facts}}
        with open("facts.json", "w") as file:
            json.dump(facts_states, file, indent=4)
        expert_system.infer()
        result = expert_system.potentiel_pannes
        return render_template('resultat.html', result=result)
    else:
        return redirect(url_for('accueil'))

@app.route('/add_rule', methods=['POST'])
def add_rule():
        rule_name = request.form['rule_name']
        conditions = request.form['conditions'].split(',')
        conclusion = request.form['conclusion']
        rules[rule_name] = {
            'conditions': conditions,
            'conclusion': conclusion
        }
        for condition in conditions:
            facts[condition] = False
        data['rules'] = rules
        data['facts'] = facts
        with open('data.json', 'w') as file:
            json.dump(data, file, indent=4)
        return redirect(url_for('admin'))

@app.route('/delete_rule/<rule_name>', methods=['POST'])
def delete_rule(rule_name):
    if request.method == 'POST':
        if rule_name in rules:
            del rules[rule_name]
            data['rules'] = rules
            with open('data.json', 'w') as file:
                json.dump(data, file, indent=4)
    return redirect(url_for('admin'))

if __name__ == '__main__':
    data, facts, rules = read_json()
    app.run(debug=True)
    
