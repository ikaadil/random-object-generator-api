from flask import Flask, jsonify

from service import generate_file


app = Flask(__name__)

@app.route('/generate', methods=['POST'])
def upload():
    response = generate_file()

    return jsonify({"response": response})


if __name__ == '__main__':
    app.run()
