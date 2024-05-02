from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/report', methods=['GET', 'POST'])
def report():
    return render_template('report.html')

@app.route('/behaviour_analysis', methods=['GET', 'POST'])
def behaviour_analysis():
    return render_template('behaviour_analysis.html')

@app.route('/popularity', methods=['GET', 'POST'])
def popularity():
    return render_template('popularity.html')

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000, debug=True)
 