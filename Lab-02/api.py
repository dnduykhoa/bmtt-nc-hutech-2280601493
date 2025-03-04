from flask import Flask, request, jsonify
from cipher.caesar import CaesarCipher
from cipher.vigenere import VigenereCipher
from cipher.railfence import RailFenceCipher
app = Flask(__name__)

caesar_cipher = CaesarCipher()

@app.route('/api/caesar/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = caesar_cipher.encrypt_text(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/caesar/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    encrypted_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = caesar_cipher.decrypt_text(encrypted_text, key)
    return jsonify({'decrypted_message': decrypted_text})


vigenere_cipher = VigenereCipher()

@app.route('/api/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = data['key']
    encrypted_text = vigenere_cipher.vigenere_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    encrypted_text = data['cipher_text']
    key = data['key']
    decrypted_text = vigenere_cipher.vigenere_decrypt(encrypted_text, key)
    return jsonify({'decrypted_message': decrypted_text})

railfence_cipher = RailFenceCipher()

@app.route('/api/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    plain_text = data['plain_text']
    key = int(data['key'])
    encrypted_text = railfence_cipher.rail_fence_encrypt(plain_text, key)
    return jsonify({'encrypted_message': encrypted_text})

@app.route('/api/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    encrypted_text = data['cipher_text']
    key = int(data['key'])
    decrypted_text = railfence_cipher.rail_fence_decrypt(encrypted_text, key)
    return jsonify({'decrypted_message': decrypted_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5001, debug=True)