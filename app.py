from flask import Flask, abort, request, jsonify, g, url_for, render_template

# initialization
app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/getName')
def get_name():
    print("in getName view....")
    output = {"name": ""}
    return jsonify(output)

if __name__ == '__main__':
    if not os.path.exists('db.sqlite'):
        db.create_all()
    app.run(debug=True)
