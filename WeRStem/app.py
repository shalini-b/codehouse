from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('index.html')


@app.route('/animal_facts/')
def animal_facts():
    return render_template('animal_facts.html')


if __name__ == '__main__':
    app.run()
