
from flask import *
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/add_todo')
def add_todo():
    item = request.args.get('item')
    return item


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')