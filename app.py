from flask import Flask, jsonify, render_template
from service import generate_file_and_report
app = Flask(__name__, static_folder="templates")


@app.route('/', methods=['GET'])
def index():
    return render_template('index.html')


@app.route('/generate', methods=['GET'])
def upload():
    response = generate_file_and_report()

    if response:
        return jsonify({"response": response}), 200
    else:
        return "File has not been generated", 400


if __name__ == '__main__':
    app.run(debug=True)
