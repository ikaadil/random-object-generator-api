from flask import Flask, jsonify, send_file
from service import generate_file
app = Flask(__name__)


@app.route('/generate', methods=['POST'])
def upload():
    response = generate_file()
    return jsonify({"response": response})


@app.route('/download/<path:path>', methods=['GET'])
def download_file(path):
    return send_file(path, as_attachment=True)


if __name__ == '__main__':
    app.run(port=5000, debug=True)
