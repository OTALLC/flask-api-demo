from flask import Flask, request, jsonify
import hashlib

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hey there, world!'

@app.route('/uppercase/<input_string>')
def to_uppercase(input_string):
    # Convert the input string to uppercase
    if input_string.isalpha():
        uppercase_string = input_string.upper()
        # Return the modified string
        return uppercase_string
    else:
        return "Error: The input contains non-letter characters. Please provide a string with letters only."

known_good_hashes = {
    'd41d8cd98f00b204e9800998ecf8427e',
    '486eb65274adb86441072afa1e2289f3'
}

@app.route('/check_hash', methods=['POST'])
def check_hash():
    data = request.json
    if 'input_string' not in data:
        return jsonify({"error": "input_string not provided"}), 400

    input_string = data['input_string']

    hash_object = hashlib.md5(input_string.encode())
    input_hash = hash_object.hexdigest()

    if input_hash in known_good_hashes:
        return jsonify({"result": "Match!", "hash": input_hash})
    else:
        return jsonify({"result": "No matching hash", "Your string hash": input_hash})



if __name__ == '__main__':
    app.run(debug=True, port=8000)
