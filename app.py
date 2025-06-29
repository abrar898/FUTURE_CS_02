from flask import Flask, redirect, request, render_template, send_file, url_for
import os
from encryption import encrypt_file, decrypt_file

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
DECRYPTED_FOLDER = 'decrypted'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
os.makedirs(DECRYPTED_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        uploaded_file = request.files['file']
        filename = uploaded_file.filename
        file_path = os.path.join(UPLOAD_FOLDER, filename)
        uploaded_file.save(file_path)

        encrypted_path = os.path.join(UPLOAD_FOLDER, f'encrypted_{filename}')        
        encrypt_file(file_path, encrypted_path)
        os.remove(file_path)

        # return f'File uploaded and encrypted as: {encrypted_path}'
        return redirect(url_for('view_files'))
    return render_template('index.html')
@app.route('/files')
def view_files():
    files = [f for f in os.listdir(UPLOAD_FOLDER) if  f.startswith("encrypted_")]
    return render_template('files.html', files=files)

@app.route('/download/<filename>', methods=['GET'])
def download(filename):
    encrypted_path = os.path.join(UPLOAD_FOLDER, filename)
    
    # Just send the encrypted file directly
    if os.path.exists(encrypted_path):
        return send_file(encrypted_path, as_attachment=True)
    else:
        return "Encrypted file not found", 404
@app.route('/decrypt/<filename>', methods=['GET'])
def decrypt_and_prepare(filename):
    encrypted_path = os.path.join(UPLOAD_FOLDER, filename)
    decrypted_path = os.path.join(DECRYPTED_FOLDER, f'decrypted_{filename}')

    if os.path.exists(encrypted_path):
        decrypt_file(encrypted_path, decrypted_path)
        return send_file(decrypted_path, as_attachment=True)
    else:
        return "Encrypted file not found", 404
if __name__ == '__main__':
    app.run(debug=True)
